import arcade
from windows import Comp151Window

def main():
    window = Comp151Window(800,800)
    arcade.set_background_color(arcade.color.SEA_BLUE)
    window.setup()
    arcade.run()

main()
