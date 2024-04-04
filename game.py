from pygame import *

window = display.set_mode((1000, 1200))
display.set_caption('Ping-Pong')

clock = time.Clock()

background = transform.scale(
        image.load('table.png'),
        (100, 1200)
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
        if keys_pressed[K_s] and self.rect.y > 1150:
            self.rect.y += self.speed
#class Ball(GameSprite):
#


run = True
while run:
    for event in event.get():
        if event.type == QUIT:
            run = False 

    window.blit(background, (0, 0))

    clock.tick(40)
    display.update()