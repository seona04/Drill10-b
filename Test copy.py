from pico2d import *
import random
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(
            self.frame * 100, 0, 100, 100,
            self.x, self.y
        )





class Ball:
    def __init__(self):
        self.size = random.choice([21, 41])

        if self.size == 21:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x = random.randint(21, 779)
        self.y = 599

        self.speed = random.uniform(2.0, 8.0)

        self.ground_y = 55 + self.size / 2
    def update(self):
        # 바닥에 도착하기 전까지 낙하
        if self.y > self.ground_y:
            self.y -= self.speed

 
    def draw(self):
        self.image.draw(self.x, self.y)
        




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