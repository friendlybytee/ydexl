import arcade
from arcade.types import Color

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying squares"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, side, color):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.side = side
        self.color = color

    def setup(self):
        x = (self.width - self.side) // 2
        self.points = [[x, 0], [x, 0]]

    def on_draw(self):
        self.clear()
        c = Color.from_hex_string(self.color)
        for p in self.points:
            arcade.draw_lbwh_rectangle_filled(p[0], p[1], self.side, self.side, c)

    def on_update(self, delta_time):
        self.points[0][0] -= 2
        self.points[0][1] += 2
        self.points[1][0] += 2
        self.points[1][1] += 2


def setup_game(width=900, height=600, title="Flying squares", side=100, color="#ff40ff"):
    game = MyGame(width, height, title, side, color)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
