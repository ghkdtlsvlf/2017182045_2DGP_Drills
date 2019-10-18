from pico2d import *
import random


# Game object class here

class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.Small_bx, self.Small_by = random.randint(0, 700), random.randint(300, 599)

    def update(self):
        if self.Small_by > 60:
            self.Small_by -= random.randint(3, 20)

    def draw(self):
        self.image.draw(self.Small_bx, self.Small_by)


class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.Big_bx, self.Big_by = random.randint(0, 700), random.randint(300, 599)

    def update(self):
        if self.Big_by > 70:
            self.Big_by -= random.randint(2, 10)

    def draw(self):
        self.image.draw(self.Big_bx, self.Big_by)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code

open_canvas()

team = [Boy() for i in range(11)]

Big_B_Count = random.randint(5, 10)
Small_B_count = 20 - Big_B_Count

Big_B_Array = [Big_Ball() for i in range(Big_B_Count)]
Small_B_Array = [Small_Ball() for i in range(Small_B_count)]

grass = Grass()

running = True

# game main loop code

while running:
    handle_events()

    for boy in team:
        boy.update()

    for BigBall in Big_B_Array:
        BigBall.update()

    for SmallBall in Small_B_Array:
        SmallBall.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    for BigBall in Big_B_Array:
        BigBall.draw()

    for SmallBall in Small_B_Array:
        SmallBall.draw()

    update_canvas()

    delay(0.05)

# finalization code

close_canvas()
