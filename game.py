from pygame import *

window = display.set_mode((874, 682))
display.set_caption('Ping-Pong')

clock = time.Clock()

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
player1 = Players('player.png', 10, 0, 341, 120, 120)
player2 = Players('player.png', 10, 770, 341, 120, 120)

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

    clock.tick(40)
    display.update()