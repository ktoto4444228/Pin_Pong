from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пин Понг')
window.fill((120, 130, 240))
game = True

clock = time.Clock()
FPS = 60

while game == True:
    display.update()
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False