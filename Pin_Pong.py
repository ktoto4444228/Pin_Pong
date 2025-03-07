from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пин Понг')
window.fill((120, 130, 240))
game = True

font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 47)
text_render = font1.render('Счет:' + str(0), 1, (255, 255, 255))
text_render2 = font1.render('Счет:' + str(0), 1, (255, 255, 255))
text_render3 = font2.render('Победил игрок за красную платформу!', 1, (255, 0, 0))
text_render4 = font2.render('Победил игрок за синюю платформу!', 1, (0, 0, 255))

slovar = {}

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_width, player_height, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.schet = 0
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
        if ball.rect.x > 650 or ball.rect.x < 0:
            self.speed_x *= -1

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

player1 = Player1('palkared.png', 6, 30, 85, 100, 150)
player2 = Player2('palkablue.png', 6, 30, 85, 500, 150)
ball = Ball('teniss_boll.png', 5, 360, 160, 150)

players = sprite.Group()
players.add(player1)
players.add(player2)

schet = 0

while game == True:
    display.update()
    window.fill((120, 130, 240))
    clock.tick(FPS)
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    ball.update()
    window.blit(text_render, (0,0))
    window.blit(text_render2, (600, 0))
    if ball.rect.x > 650:
        player1.schet += 1
        text_render = font1.render('Счет:' + str(player1.schet), 1, (255, 255, 255))
        ball.rect.x = 350
        ball.rect.y = 250
    if ball.rect.x < 0:
        player2.schet += 1
        text_render2 = font1.render('Счет:' + str(player2.schet), 1, (255, 255, 255))
        ball.rect.x = 350
        ball.rect.y = 250
    for m in sprite.spritecollide(ball, players, False):
        if schet > 20:
            ball.speed_x *= -1
            schet = 0
    schet += 1
    if player1.schet > 4:
        window.blit(text_render3, (0, 150))
    if player2.schet > 4:
        window.blit(text_render4, (0, 150))
    for e in event.get():
        if e.type == QUIT:
            game = False
