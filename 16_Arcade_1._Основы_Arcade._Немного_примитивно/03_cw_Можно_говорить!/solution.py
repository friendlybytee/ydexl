import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smile Silence"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.radius = radius

    def on_draw(self):
        self.clear()
        x = self.width // 2
        y = self.height // 2
        r = self.radius
        arcade.draw_circle_filled(x, y, r, (255, 192, 0))
        arcade.draw_circle_filled(x - r // 2, y + r // 2, 15, arcade.color.BLACK)
        arcade.draw_circle_filled(x + r // 2, y + r // 2, 15, arcade.color.BLACK)
        arcade.draw_arc_outline(x, y, r * 3 // 2, r * 3 // 2, arcade.color.BLACK, 180, 360, r // 20)


def setup_game(width=800, height=600, title="Smile Silence", radius=200):
    game = MyGame(width, height, title, radius)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
