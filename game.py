from pygame import *

window = display.set_mode((874, 682))
display.set_caption('Ping-Pong')
font.init()
clock = time.Clock()
p1score = 0
p2score = 0
font1 = font.SysFont('Arial', 40)
p1win = font1.render('Игрок 1 победил', True, (0, 255, 0))
p2win = font1.render('Игрок 2 победил', True, (0, 255, 0))
p1scoretxt = font1.render(str(p1score), True, (0, 0, 0))
p2scoretxt = font1.render(str(p2score), True, (0, 0, 0))
background = transform.scale(
        image.load('table.png'),
        (874, 682)
    )
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, posX, posY, sizeX, sizeY):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(sizeX, sizeY))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Players(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 570:
            self.rect.y += self.speed
    def updatep2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 570:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, speed, posX, posY, sizeX, sizeY):
        super().__init__(player_image, speed, posX, posY, sizeX, sizeY)
        self.velX = speed
        self.velY = speed
           
    def update(self):
        global run
        if sprite.collide_rect(player1, ball):
            self.velX *= -1
            p1score += 1
        if sprite.collide_rect(player2, ball):
            self.velX *= -1
            p2score += 1

        self.rect.x += self.velX
        self.rect.y += self.velY

        if self.rect.y >= 652 or self.rect.y <= 0:
            self.velY *= -1
        if self.rect.x >= 844 or self.rect.x <= 0:
            self.velX *= -1
        
        if self.rect.x <= 0:
            window.blit(p2win, (337, 341))
            run = False
        if self.rect.x >= 844:
            window.blit(p1win, (337, 341))
            run = False

        

player1 = Players('player.png', 10, 0, 341, 120, 120)
player2 = Players('player.png', 10, 770, 341, 120, 120)
ball = Ball('ball.png', 3, 50, 50, 90, 90)

init()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False 

    window.blit(background, (0, 0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.updatep2()
    ball.reset()
    ball.update()
    window.blit(p1scoretxt, 20, 10)
    window.blit(p2scoretxt, 600, 10)

    clock.tick(40)
    display.update()