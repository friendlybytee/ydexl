import arcade

PART = 20
SCREEN_WIDTH = PART * 36
SCREEN_HEIGHT = PART * 15
SCREEN_TITLE = "Flying storks"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.part = part

    def setup(self):
        n = self.width / self.part
        self.storks = [0, n / 2, n]

    def on_draw(self):
        self.clear()
        for x in self.storks:
            self.draw_stork(x)

    def draw_stork(self, x):
        p = self.part
        b = p / 10
        w = arcade.color.WHITE
        k = arcade.color.BLACK
        r = arcade.color.RED
        arcade.draw_triangle_filled(x * p, 11 * p, (x + 2) * p, 11.3 * p, (x + 2) * p, 10.7 * p, r)
        arcade.draw_circle_filled((x + 3) * p, 11 * p, p, w)
        arcade.draw_circle_outline((x + 3) * p, 11 * p, p, k, b)
        arcade.draw_circle_filled((x + 3) * p, 11 * p, 0.3 * p, k)
        arcade.draw_arc_filled((x + 10) * p, 11 * p, 4 * p, 4 * p, w, 180, 360)
        arcade.draw_arc_outline((x + 10) * p, 11 * p, 4 * p, 4 * p, k, 180, 360, b)
        arcade.draw_line((x + 4) * p, 11 * p, (x + 16) * p, 11 * p, k, b)
        arcade.draw_line((x + 4) * p, 10.7 * p, (x + 8) * p, 10.7 * p, k, b)
        arcade.draw_line((x + 12) * p, 11 * p, (x + 16) * p, 10 * p, k, b)
        arcade.draw_arc_filled((x + 11.5) * p, 11.5 * p, 3 * p, 3 * p, k, 45, 225)
        arcade.draw_circle_filled((x + 14) * p, 11 * p, 0.2 * p, r)
        arcade.draw_circle_filled((x + 14) * p, 10.5 * p, 0.2 * p, r)
        arcade.draw_triangle_filled((x + 16) * p, 11 * p, (x + 16.5) * p, 11.3 * p, (x + 16.5) * p, 10.7 * p, r)
        arcade.draw_triangle_filled((x + 16) * p, 10 * p, (x + 16.5) * p, 10.3 * p, (x + 16.5) * p, 9.7 * p, r)

    def on_update(self, delta_time):
        n = self.width / self.part
        for i in range(3):
            self.storks[i] -= 0.05
            if self.storks[i] <= -n / 2:
                self.storks[i] += n * 1.5


def setup_game(width=720, height=300, title="Flying storks", part=20):
    game = MyGame(width, height, title, part)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
