from pico2d import *
import random
class Grass:

        pass


class Boy:



class Ball:



def reset_world():


def update_world():
 

def render_world():
    clear_canvas()

    update_canvas()


def handle_events():
    global running

    running = False


def main():
    open_canvas()
    reset_world()

    while running:
        handle_events()
        update_world()
        render_world()
        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()