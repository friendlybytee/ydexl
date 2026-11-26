import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Perspective"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, width_rect, height_rect, color_rect):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.width_rect = width_rect
        self.height_rect = height_rect
        self.color_rect = color_rect

    def on_draw(self):
        self.clear()
        x = (self.width - self.width_rect) // 2
        r, g, b = self.color_rect
        for i in range(3, -1, -1):
            c = (r - 20 * i, g - 20 * i, b)
            arcade.draw_lbwh_rectangle_filled(x + 20 * i, 20 + 20 * i, self.width_rect - 40 * i, self.height_rect, c)


def setup_game(width=900, height=600, title="Perspective", width_rect=500, height_rect=300, color_rect=(192, 255, 0)):
    game = MyGame(width, height, title, width_rect, height_rect, color_rect)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
