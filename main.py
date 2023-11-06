from ursina import *
from Scripts.State import menu


app = Ursina()
window.borderless = False
window.exit_button.disable()

menu.run(app)


def update():
    menu.update()


def input(key):
    menu.input(key)


app.run()
