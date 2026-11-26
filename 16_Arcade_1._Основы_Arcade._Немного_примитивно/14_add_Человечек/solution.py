import arcade

PART = 30
SCREEN_WIDTH = PART * 12
SCREEN_HEIGHT = PART * 11
SCREEN_TITLE = "Walking man"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BRILLIANT_LAVENDER)
        self.part = part

    def setup(self):
        self.hands = [4, 5]
        self.foots = [4, 2]
        self.i = 0
        self.d = 1

    def on_draw(self):
        self.clear()
        p = self.part
        k = arcade.color.BLACK
        t = p / 4
        hx = self.hands[0]
        fx = self.foots[0]
        rx = 12 - fx
        arcade.draw_line(p, 2 * p, 11 * p, 2 * p, k, p / 10)
        arcade.draw_circle_filled(6 * p, 9 * p, p / 2, k)
        arcade.draw_line(6 * p, 9 * p, 6 * p, 5 * p, k, t)
        arcade.draw_line(6 * p, 8 * p, hx * p, self.hands[1] * p, k, t)
        arcade.draw_line(6 * p, 8 * p, (12 - hx) * p, self.hands[1] * p, k, t)
        arcade.draw_line(6 * p, 5 * p, fx * p, self.foots[1] * p, k, t)
        arcade.draw_line(6 * p, 5 * p, rx * p, self.foots[1] * p, k, t)
        arcade.draw_line(fx * p, 2 * p, (fx + 1) * p, 2 * p, k, t)
        arcade.draw_line(rx * p, 2 * p, (rx + 1) * p, (2 + (rx - 6) / 2) * p, k, t)

    def on_update(self, delta_time):
        self.i += 1
        if self.i % 10 == 0:
            self.hands[0] += self.d
            self.foots[0] += self.d
            if self.foots[0] == 6 or self.foots[0] == 4:
                self.d = -self.d


def setup_game(width=360, height=330, title="Walking man", part=30):
    game = MyGame(width, height, title, part)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
