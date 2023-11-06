from ursina import *
from Scripts.Proc.WorldGen.perlin import generate_fractal_noise_2d
import time
from math import pi

# start = time.perf_counter()
# size = 1000


def create_perlin(size, fallout=True) -> list[list[float]]:
    start = time.perf_counter()
    octave = 3
    print(octave)
    pic = generate_fractal_noise_2d(
        shape=(size, size),
        res=(1, 1),
        octaves=octave,
        tileable=(True, True)
    )
    # Falloff map
    if fallout:
        for s, i in enumerate(pic):
            for r, j in enumerate(i):
                pic[s][r] -= ((s+r)/550)

    print(f'Heightmap generated in {time.perf_counter() - start:.2f}s')
    return pic


# app = Ursina()
def render_world(pic, size) -> tuple[Entity, Entity]:
    start = time.perf_counter()
    z = []
    plane = Plane(subdivisions=(size-1, size-1))
    for r, i in enumerate(plane.vertices):
        z.append(Vec3(i.x, pic[r // size][r % size] / 4, i.z))
    plane.vertices = z
    print(f'World Rendered in {time.perf_counter() - start:.2f}s')

    colors = []
    for i in z:
        if i.y >= 0.02:
            colors.append(color.rgba(0, 154, 23))
        elif i.y >= 0:
            colors.append(color.yellow)
        else:
            colors.append(color.dark_gray)
    print(f'Generate Colors in {time.perf_counter() - start:.2f}s')

    terrain = Entity(model=Mesh(
            vertices=z,
            triangles=plane.triangles,
            uvs=plane.uvs,
            normals=plane.normals,
            colors=colors,
        ),
        scale=size,
        collider='mesh'
    )

    ocean = Entity(
        model=Plane(),
        color=color.rgba(0, 157, 196, 150),
        scale=size
    )

    print(f'Created Models in {time.perf_counter() - start:.2f}s')


# EditorCamera()
    end = time.perf_counter()
    print(f'Generated a {size}x{size} world in {end - start:.2f}s')
    return terrain, ocean
# app.run()


def create_world(size) -> tuple[Entity, Entity]:
    return render_world(create_perlin(size), size)


if __name__ == '__main__':
    world_size = 300
    app = Ursina()
    render_world(create_perlin(world_size), world_size)
    # player = FirstPersonController()
    # player.y = 200
    EditorCamera()
    app.run()
