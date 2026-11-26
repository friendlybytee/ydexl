import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Balls"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.radius = radius

    def setup(self):
        r = self.radius
        self.balls = []
        for i in range(12):
            x = random.randint(r, self.width - r)
            y = random.randint(r, self.height - r)
            self.balls.append([x, y])
        self.change = []
        for i in range(12):
            dx = random.randint(-3, 3)
            dy = random.randint(-3, 3)
            self.change.append([dx, dy])
        c = arcade.color
        self.colors = [c.SAE, c.AMBER, c.AMETHYST, c.APPLE_GREEN, c.AZURE, c.BALL_BLUE,
                       c.BRIGHT_LILAC, c.BITTERSWEET, c.BLUE_VIOLET, c.BRIGHT_PINK, c.CITRINE, c.FRENCH_LIME]

    def on_draw(self):
        self.clear()
        for i in range(12):
            arcade.draw_circle_filled(self.balls[i][0], self.balls[i][1], self.radius, self.colors[i])

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
