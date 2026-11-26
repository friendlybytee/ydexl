import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Boms"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, start_radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.start_radius = start_radius

    def setup(self):
        self.circle_radius = [self.start_radius, 0]
        self.colors = [arcade.color.WHITE, arcade.color.BLACK]
        self.circle_change = 1

    def on_draw(self):
        self.clear()
        for i in range(len(self.circle_radius)):
            arcade.draw_circle_filled(self.width / 2, self.height / 2, self.circle_radius[i], self.colors[i])

    def on_update(self, delta_time):
        for i in range(len(self.circle_radius)):
            self.circle_radius[i] += self.circle_change
        if self.circle_radius[-1] >= self.start_radius:
            if self.colors[-1] == arcade.color.BLACK:
                self.colors.append(arcade.color.WHITE)
            else:
                self.colors.append(arcade.color.BLACK)
            self.circle_radius.append(0)
        if self.circle_radius[1] > self.width + self.height:
            self.circle_radius.pop(0)
            self.colors.pop(0)


def setup_game(width=800, height=600, title="Boms", start_radius=50):
    game = MyGame(width, height, title, start_radius)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
