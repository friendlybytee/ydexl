import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Balls"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.radius = radius

    def setup(self):
        self.balls = []
        for i in range(12):
            self.balls.append([self.width / 2, self.height / 2])
        self.change = [[1, 1], [1, -1], [-1, 1], [-1, -1],
                       [2, 1], [2, -1], [-2, 1], [-2, -1],
                       [1, 2], [1, -2], [-1, 2], [-1, -2]]

    def on_draw(self):
        self.clear()
        for b in self.balls:
            arcade.draw_circle_filled(b[0], b[1], self.radius, arcade.color.WHITE)

    def on_update(self, delta_time):
        r = self.radius
        for i in range(12):
            b = self.balls[i]
            c = self.change[i]
            b[0] += c[0]
            b[1] += c[1]
            if b[0] - r <= 0 or b[0] + r >= self.width:
                c[0] = -c[0]
            if b[1] - r <= 0 or b[1] + r >= self.height:
                c[1] = -c[1]


def setup_game(width=800, height=600, title="Balls", radius=10):
    game = MyGame(width, height, title, radius)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
