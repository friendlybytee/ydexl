import arcade

PART = 20
SCREEN_WIDTH = PART * 30
SCREEN_HEIGHT = PART * 15
SCREEN_TITLE = "Running mouse"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ANDROID_GREEN)
        self.part = part

    def setup(self):
        self.point = 3
        self.i = 0

    def on_draw(self):
        self.clear()
        self.draw_head(self.point)
        self.draw_body(self.point, self.i)
        self.draw_tail(self.point)

    def draw_head(self, x):
        p = self.part
        arcade.draw_triangle_filled(x * p, 10 * p, (x + 5.5) * p, 12 * p, (x + 6) * p, 5 * p, arcade.color.GRAY)
        arcade.draw_circle_filled(x * p, 10 * p, 1.5 * p, arcade.color.GRAY)
        arcade.draw_circle_filled((x + 0.75) * p, 10 * p, 0.75 * p, arcade.color.PINK)
        arcade.draw_circle_filled((x + 5) * p, 13 * p, 1.5 * p, arcade.color.GRAY)
        arcade.draw_circle_filled((x + 4.5) * p, 12.5 * p, 0.75 * p, arcade.color.PINK)
        arcade.draw_circle_filled((x + 3) * p, 9.5 * p, 0.2 * p, arcade.color.BLACK)
        arcade.draw_circle_filled((x + 4) * p, 10 * p, 0.2 * p, arcade.color.BLACK)
        arcade.draw_circle_filled((x + 6) * p, 5 * p, 0.2 * p, arcade.color.BLACK)
        arcade.draw_line((x + 5.25) * p, 5 * p, (x + 6.75) * p, 5 * p, arcade.color.BLACK, 0.1 * p)
        arcade.draw_line((x + 5.5) * p, 4.5 * p, (x + 6.5) * p, 5.5 * p, arcade.color.BLACK, 0.1 * p)

    def draw_body(self, x, i):
        p = self.part
        if i == 0:
            arcade.draw_triangle_filled((x - 2) * p, 3 * p, (x + 3) * p, p, (x + 3) * p, 7.5 * p, arcade.color.GRAY)
        else:
            arcade.draw_triangle_filled(x * p, p, (x + 6) * p, p, (x + 2.5) * p, 7.5 * p, arcade.color.GRAY)

    def draw_tail(self, x):
        p = self.part
        arcade.draw_arc_outline((x - 3) * p, 6 * p, 2 * p, 2 * p, arcade.color.BLACK, 0, 90, 0.2 * p)
        arcade.draw_line((x - 2) * p, 6 * p, (x - 1) * p, 2 * p, arcade.color.BLACK, 0.1 * p)
        arcade.draw_arc_outline(x * p, 2 * p, 2 * p, 2 * p, arcade.color.BLACK, 180, 360, 0.2 * p)
        arcade.draw_line((x + 1) * p, 2 * p, (x + 1) * p, 3 * p, arcade.color.BLACK, 0.1 * p)

    def on_update(self, delta_time):
        self.point += 0.05
        self.i = int(self.point) % 2
        if (self.point - 3) * self.part >= self.width:
            self.point = 3


def setup_game(width=600, height=300, title="Running mouse", part=20):
    game = MyGame(width, height, title, part)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
