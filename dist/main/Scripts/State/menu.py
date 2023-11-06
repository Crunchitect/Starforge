from ursina import destroy, EditorCamera, Text, Button, Entity, color
from ursina.prefabs.first_person_controller import FirstPersonController
from Scripts.Abstraction import select_sector
from ursina import Ursina

state = ...
play_button, play_icon, game_name, play_text = ..., ..., ..., ...
editor_button, editor_icon, editor_text = ..., ..., ...
cam = ...
app = ...


def play_game():
    global state, play_button, play_icon, game_name, play_text, editor_button, editor_icon, editor_text, cam, app
    cam = EditorCamera()
    select_sector.run(cam, app)
    state = "Play"
    try:
        destroy(play_button)
        destroy(play_icon)
        destroy(game_name)
        destroy(play_text)
        destroy(editor_icon)
        destroy(editor_text)
        destroy(editor_button)
        del play_button, play_icon, game_name, play_text, editor_button, editor_icon, editor_text
    except NameError:
        pass


def run(get_app: Ursina):
    global state, play_button, play_icon, game_name, play_text, editor_button, editor_icon, editor_text, app

    app = get_app

    state = "Menu"
    game_name = Text(
        text="STARFORGE",
        font="Fonts/font.ttf",
        x=-.25,
        y=0.3,
        z=-3,
        scale=3
    )

    play_button = Button(
        text=(play_text := Text(
            text="Play",
            font="Fonts/font.ttf",
            position=(-.025+-.1, -0.02, -2),
            scale=.75
        )),
        scale=.1,
        on_click=play_game,
        x=-.1,
    )

    play_icon = Entity(
        model='quad',
        texture="Sprites/play_button.png",
        parent=play_button,
        scale=.5,
        y=.08
    )

    editor_button = Button(
        text=(editor_text := Text(
            text="Edit",
            font="Fonts/font.ttf",
            position=(-.025 + .1, -0.02, -2),
            scale=.75
        )),
        scale=.1,
        x=.1,
    )

    editor_icon = Entity(
        model='quad',
        texture="Sprites/editor.png",
        parent=editor_button,
        scale=.5,
        y=.08,
        color=color.rgb(255, 255, 255)
    )


def update():
    if state == "Play":
        select_sector.update(cam)


def input(key):
    from Scripts.Abstraction.select_sector import cam_state
    global cam
    if cam_state == 'fpc' or cam_state == 'e-cam':
        cam.eternal = False
    if cam_state == 'fpc' and key == 'escape':
        if isinstance(cam, EditorCamera):
            cam.ignore = True
            destroy(cam)
            cam = FirstPersonController()
        else:
            cam.ignore = False
        cam.enabled = False
        cam.ignore = True
    if cam_state == 'fpc' and key == 'tab':
        if isinstance(cam, EditorCamera):
            cam.ignore = True
            destroy(cam)
            cam = FirstPersonController()
        else:
            cam.ignore = False
        cam.enabled = True
        cam.ignore = False
    if cam_state == 'e-cam':
        if isinstance(cam, FirstPersonController):
            cam.ignore = True
            destroy(cam)
            cam = EditorCamera()
        else:
            cam.ignore = False
        cam.enabled = True
        cam.ignore = False
