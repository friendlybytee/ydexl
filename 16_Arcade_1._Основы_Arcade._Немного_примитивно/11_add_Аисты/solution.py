import arcade

PART = 20
SCREEN_WIDTH = PART * 20
SCREEN_HEIGHT = PART * 20
SCREEN_TITLE = "Storks"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
        self.part = part

    def on_draw(self):
        self.clear()
        p = self.part
        b = p / 10
        l = p / 5
        w = arcade.color.WHITE
        k = arcade.color.BLACK
        r = arcade.color.RED

        arcade.draw_triangle_filled(0, 16 * p, 2 * p, 16.3 * p, 2 * p, 15.7 * p, r)
        arcade.draw_circle_filled(3 * p, 16 * p, p, w)
        arcade.draw_circle_outline(3 * p, 16 * p, p, k, b)
        arcade.draw_circle_filled(3 * p, 16 * p, 0.3 * p, k)
        arcade.draw_arc_filled(10 * p, 16 * p, 4 * p, 4 * p, w, 180, 360)
        arcade.draw_arc_outline(10 * p, 16 * p, 4 * p, 4 * p, k, 180, 360, b)
        arcade.draw_line(4 * p, 16 * p, 16 * p, 16 * p, k, l)
        arcade.draw_line(4 * p, 15.7 * p, 8 * p, 15.7 * p, k, l)
        arcade.draw_line(12 * p, 16 * p, 16 * p, 15 * p, k, l)
        arcade.draw_arc_filled(11.5 * p, 16.5 * p, 3 * p, 3 * p, k, 45, 225)
        arcade.draw_circle_filled(14 * p, 16 * p, 0.2 * p, r)
        arcade.draw_circle_filled(14 * p, 15.5 * p, 0.2 * p, r)
        arcade.draw_triangle_filled(16 * p, 16 * p, 16.5 * p, 16.3 * p, 16.5 * p, 15.7 * p, r)
        arcade.draw_triangle_filled(16 * p, 15 * p, 16.5 * p, 15.3 * p, 16.5 * p, 14.7 * p, r)

        arcade.draw_triangle_filled(0, 11 * p, 2 * p, 12 * p, 2 * p, 11.5 * p, r)
        arcade.draw_circle_filled(3 * p, 12 * p, p, w)
        arcade.draw_circle_outline(3 * p, 12 * p, p, k, b)
        arcade.draw_circle_filled(3 * p, 12 * p, 0.3 * p, k)
        arcade.draw_line(3 * p, 11 * p, 3 * p, 8 * p, k, l)
        arcade.draw_line(3.3 * p, 11 * p, 3.3 * p, 8 * p, k, l)
        arcade.draw_line(4.5 * p, 6 * p, 4.5 * p, 2 * p, k, l)
        arcade.draw_line(5.5 * p, 6 * p, 5.5 * p, 2 * p, k, l)
        arcade.draw_circle_filled(4.5 * p, 4 * p, 0.2 * p, r)
        arcade.draw_circle_filled(5.5 * p, 4 * p, 0.2 * p, r)
        arcade.draw_triangle_filled(4.5 * p, 2.5 * p, 4.2 * p, 2 * p, 4.8 * p, 2 * p, r)
        arcade.draw_triangle_filled(5.5 * p, 2.5 * p, 5.2 * p, 2 * p, 5.8 * p, 2 * p, r)
        arcade.draw_arc_filled(5 * p, 8 * p, 4 * p, 4 * p, w, 180, 360)
        arcade.draw_arc_outline(5 * p, 8 * p, 4 * p, 4 * p, k, 180, 360, b)
        arcade.draw_line(3 * p, 8 * p, 7 * p, 8 * p, k, l)
        arcade.draw_arc_filled(5.5 * p, 8.5 * p, 3 * p, 3 * p, k, 45, 225)

        arcade.draw_line(12 * p, 6 * p, 11 * p, 2 * p, k, l)
        arcade.draw_line(12 * p, 6 * p, 13 * p, 2 * p, k, l)
        arcade.draw_circle_filled(11.5 * p, 4 * p, 0.2 * p, r)
        arcade.draw_circle_filled(12.5 * p, 4 * p, 0.2 * p, r)
        arcade.draw_triangle_filled(11 * p, 2.5 * p, 10.75 * p, 2 * p, 11.25 * p, 2 * p, r)
        arcade.draw_triangle_filled(13 * p, 2.5 * p, 12.75 * p, 2 * p, 13.25 * p, 2 * p, r)
        arcade.draw_arc_filled(12.5 * p, 8.5 * p, 3 * p, 3 * p, k, 45, 225)
        arcade.draw_arc_filled(12 * p, 6 * p, 4 * p, 4 * p, w, 0, 180)
        arcade.draw_arc_outline(12 * p, 6 * p, 4 * p, 4 * p, k, 0, 180, b)
        arcade.draw_arc_filled(10.5 * p, 8.5 * p, 3 * p, 3 * p, k, 135, 315)
        arcade.draw_line(10 * p, 6 * p, 17 * p, 6 * p, k, l)
        arcade.draw_line(14 * p, 6.3 * p, 16.25 * p, 6.3 * p, k, l)
        arcade.draw_triangle_filled(19 * p, 5 * p, 17.5 * p, 6.25 * p, 17.9 * p, 6.5 * p, r)
        arcade.draw_circle_filled(17 * p, 7 * p, p, w)
        arcade.draw_circle_outline(17 * p, 7 * p, p, k, b)
        arcade.draw_circle_filled(17 * p, 7 * p, 0.3 * p, k)


def setup_game(width=400, height=400, title="Storks", part=20):
    game = MyGame(width, height, title, part)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
