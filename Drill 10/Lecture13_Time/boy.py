import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        boy.go_left()
        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        boy.x += boy.velocity * game_framework.frame_time
        if boy.x > 1500:
            boy.go_left()
        if boy.x < 100:
            boy.go_right()

            pass

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            if boy.frame < 4:
                boy.image.clip_draw(int(boy.frame) * 200, 400, 195, 195, boy.x, boy.y)
            elif boy.frame < 9:
                boy.image.clip_draw(int(boy.frame - 5) * 200, 200, 195, 195, boy.x, boy.y)
            elif boy.frame < 15:
                boy.image.clip_draw(int(boy.frame - 10) * 200, 000, 195, 195, boy.x, boy.y)

        else:
            if boy.frame < 4:
                boy.image_left.clip_draw(805 - (int(boy.frame) * 200), 400, 195, 190, boy.x, boy.y)
            elif boy.frame < 9:
                boy.image_left.clip_draw(805 - int(boy.frame - 5) * 200, 200, 195, 190, boy.x, boy.y)
            elif boy.frame < 14:
                boy.image_left.clip_draw(805 - (int(boy.frame - 10)) * 200, 000, 195, 190, boy.x, boy.y)


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 400
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        self.image_left = load_image('bird_animation_left.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time:%3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def go_left(self):
        self.dir = -1
        self.velocity -= RUN_SPEED_PPS
        pass

    def go_right(self):
        self.dir = 1
        self.velocity += RUN_SPEED_PPS
        pass
