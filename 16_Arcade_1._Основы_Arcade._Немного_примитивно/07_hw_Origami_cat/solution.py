import arcade

SCREEN_TITLE = "Origami Cat"
PART = 25


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BEIGE)
        self.part = part

    def on_draw(self):
        self.clear()
        lst = [
            [(1, 18), (4, 15), (2, 12)],
            [(9, 18), (6, 15), (8, 12)],
            [(4, 15), (6, 15), (8, 12), (5, 9), (2, 12)],
            [(5, 15), (5, 3)],
            [(3, 11), (5, 3), (7, 11), (5, 9)],
            [(5, 9), (7, 11), (11, 7), (9, 3), (5, 3)],
            [(11, 7), (8, 1), (11, 3)],
        ]
        p = self.part
        for a in lst:
            b = []
            for x, y in a:
                b.append((x * p, y * p))
            arcade.draw_polygon_outline(b, arcade.color.COOL_BLACK, 4)


def setup_game(width=300, height=475, title="Origami Cat", part=25):
    game = MyGame(width, height, title, part)
    return game


def main():
    setup_game(PART * 12, PART * 19, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
