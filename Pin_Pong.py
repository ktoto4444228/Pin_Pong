from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пин Понг')
window.fill((120, 130, 240))
game = True

slovar = {}

clock = time.Clock()
FPS = 60

class GameSprite():
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball():
    def __init__(self, ball_image, ball_speed_x, ball_speed_y, ball_x, ball_y):
        super().__init__()
        self.image = transform.scale(image.load(ball_image), (40, 40))
        self.speed_x = 3
        self.speed_y = 4
        self.rect = self.image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if ball.rect.y < 0 or ball.rect.y > 450:
            self.speed_y *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            self.speed_x *= -1

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > 0:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y += self.speed

player1 = Player1('raketkaluche.png', 6, 100, 150)
player2 = Player2('palkablue.png', 6, 500, 150)
ball = Ball('teniss_boll.png', 5, 360, 160, 150)

while game == True:
    display.update()
    clock.tick(FPS)
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
