import game_framework
import main_state
from pico2d import *

name = "pause_state"
image = None

blink_time = False


def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

    pass


def draw():
    clear_canvas()
    global blink_time
    if blink_time:
        image.draw(400, 300)
    main_state.boy.draw()
    main_state.grass.draw()
    update_canvas()
    pass


def update():
    global blink_time
    if blink_time:
        delay(0.5)
        blink_time = False
    else:
        delay(0.5)
        blink_time = True

    pass


def pause():
    pass


def resume():
    pass
