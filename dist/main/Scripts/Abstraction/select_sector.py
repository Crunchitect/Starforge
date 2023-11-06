from typing import Union
from ursina import Text, Button, color, Entity, camera, EditorCamera, destroy, Ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from Scripts.Abstraction import create_world_sphere
from Scripts.Abstraction import create_world_plane
from threading import Thread


globe_terrain, globe_ocean, buttons, sector_no = ..., ..., ..., ...
venus_terrain, venus_ocean, venus_buttons, venus_sector_no = ..., ..., ..., ...
sector_text, explore_button, explored_text, explored_button_text = ..., ..., ..., ...
sector_plane = ...
cam_state = ...


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def run(cam: Union[EditorCamera, FirstPersonController], app: Ursina):
    global globe_terrain, globe_ocean, sector_no, sector_text, explored_text, explore_button
    global sector_plane, explored_button_text, cam_state, buttons
    global venus_terrain, venus_ocean, venus_buttons, venus_sector_no

    (globe_terrain, globe_ocean, buttons, sector_no), (venus_terrain, venus_ocean, venus_buttons, venus_sector_no) \
        = create_world_sphere.run()
    sector_plane = {
        'earth': {},
        'venus': {}
    }

    cam = EditorCamera()
    cam.scale = 10
    cam_state = 'e-cam'

    def button_event():
        global cam_state
        # if cam_state == 'fpc':
        #     print('back to planet')
        #     back_to_planet()
        # else:
        #     print('go')
        #     add_sector()
        add_sector()

    # def back_to_planet():
    #     nonlocal cam
    #     global cam_state, globe_ocean, globe_terrain, buttons, sector_plane
    #     cam.ignore = True
    #     cam.ignore_input = True
    #     cam.eternal = False
    #     destroy(cam)
    #     cam = EditorCamera()
    #     cam.setScale(10, 10, 10)
    #     cam_state = 'e-cam'
    #     cam.enable()
    #     globe_ocean.enable()
    #     globe_terrain.enable()
    #     for i in buttons:
    #         i.enable()
    #
    #     for i in sector_plane:
    #         for j in sector_plane[i]:
    #             print(i, j)
    #             sector_plane[i][j][0].disable()
    #             sector_plane[i][j][1].disable()
    #
    #     for i in scene.entities:
    #         destroy(i)
    #
    #     app.restart()
    #     from Scripts.State.menu import play_game
    #     play_game()

    def add_sector():
        nonlocal cam
        global cam_state
        from Scripts.Proc.WorldGen.Planets.Earth.world_sphere import sector
        if sector == -1:
            return
        globe_terrain.disable()
        globe_ocean.disable()
        for i in buttons:
            i.disable()

        if sector not in sector_plane:
            loading_plane = CustomThread(target=create_world_plane.run)
            loading_plane.start()
            loading_pane = Entity(
                parent=camera.ui,
                scale=2,
                color=color.black90,
                z=-1
            )
            loading_text = Text(
                text="Loading",
                font="Fonts/font.ttf"
            )

            sector_plane['earth'][sector] = loading_plane.join()
            print(sector_plane['earth'][sector])
            loading_pane.disable()
            loading_text.disable()
            del loading_pane, loading_text
        else:
            for r, i in enumerate(sector_plane):
                for s, j in enumerate(i):
                    sector_plane[i][j].disable()

            sector_plane['earth'][sector].enable()

        cam.ignore = True
        cam.ignore_input = True
        cam.eternal = False
        destroy(cam)
        cam = FirstPersonController()
        cam.setPos(0, 100, 0)
        cam.setScale(.5, .5, .5)
        cam_state = 'fpc'

    sector_text = Text(
        text=f'Sector {sector_no}',
        font='Fonts/font.ttf',
        y=0.48,
        x=-0.85
    )

    explored_text = Text(
        text=f'Unexplored',
        font='Fonts/font.ttf',
        y=0.48,
        x=0.6,
        color=color.gray
    )

    explored_button_text = Text(
        text="Go",
        font="Fonts/font.ttf",
        z=-1,
        x=0.48,
        y=0.47
    )

    explore_button = Button(
        text=explored_button_text,
        scale=(0.15, 0.05, 1),
        x=.02+0.48,
        y=-.005+0.47,
        on_click=button_event
    )


def update(cam: Union[EditorCamera, FirstPersonController]):
    global sector_plane, sector_text, explore_button, explored_text, explored_button_text
    from Scripts.Proc.WorldGen.Planets.Earth.world_sphere import sector
    sector_text.text = f'Sector {sector}' if sector != -1 else ''
    if sector == -1:
        explore_button.disable()
        explored_button_text.disable()
        explored_text.disable()
    else:
        explore_button.enable()
        explored_button_text.enable()
        explored_text.enable()
    if sector in sector_plane:
        explored_text.text = "Explored"
        explored_text.color = color.lime
    else:
        explored_text.text = "Unexplored"
        explored_text.color = color.gray

    # if cam_state == 'fpc':
    #     explored_button_text.text = "Planet Map"
    #     explored_button_text.x = 0.43
    #     explored_button_text.scale = 0.8

    if cam_state != 'fpc':
        explored_button_text.text = "Go"
        explored_button_text.x = 0.47
        explored_button_text.scale = 1
        explore_button.enable()
        explored_button_text.enable()
        explored_text.enable()
    else:
        explore_button.disable()
        explored_button_text.disable()
        explored_text.disable()
