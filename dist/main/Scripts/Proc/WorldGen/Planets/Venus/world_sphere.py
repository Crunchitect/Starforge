from ursina import *
from math import sqrt
import noise
from Scripts.Proc.WorldGen.dist_from_tri import point_triangle_distance_Vec3

sector = -1


def do_nothing():
    pass


def create_triangle_mesh(point1, point2, point3):
    # Define the vertex positions of the triangle
    vertices = [
        point1,
        point2,
        point3,
    ]

    # Define the index order of the vertices to create the faces of the triangle
    indices = [
        0, 1, 2,
    ]

    # Define the texture coordinates of the vertices
    uvs = [
        (0, 0),
        (1, 0),
        (0, 1),
    ]

    # Calculate the normals of the triangle
    normal = (point2 - point1).cross(point3 - point1).normalized()
    normals = [
        normal,
        normal,
        normal,
    ]

    # Create a Mesh object with the vertex, index, texture coordinate, and normal data
    mesh_ = Mesh(vertices=vertices, triangles=indices, uvs=uvs, normals=normals)

    return mesh_


def point_in_tri(p: Vec3, a: Vec3, b: Vec3, c: Vec3) -> bool:
    a -= p
    b -= p
    c -= p

    u = b.cross(c)
    v = c.cross(a)
    w = a.cross(b)

    if (u.dot(v) // 0.5 * 0.5) < 0:
        return False
    if (u.dot(w) // 0.5 * 0.5) < 0:
        return False
    return True


def create_planet(size, create_buttons=True):
    global sector
    mesh_ = Cube(subdivisions=(5, 5, 5))
    z = []
    sphere = []
    for i in mesh_.vertices:
        z.append(i / sqrt(i.x ** 2 + i.y ** 2 + i.z ** 2))
        sphere.append(i / sqrt(i.x ** 2 + i.y ** 2 + i.z ** 2))

    col = []
    for i in z:
        val = 1 + ((noise.pnoise3(i.x, i.y, i.z)) / 8)
        i *= val
        if val <= 0.95:
            col.append(color.rgba(147, 185, 92))
        elif val <= 1.03:
            col.append(color.rgba(247, 207, 119))
        else:
            col.append(color.rgba(245, 217, 157))
    buttons = []
    if create_buttons:
        buttons = []
        for r, i in enumerate(mesh_.triangles):
            def callr():
                global sector
                min_dist = inf
                min_dist_sector = -1
                for rx, ix in enumerate(mesh_.triangles):
                    # # print(mouse.world_point, sphere[ix[0]] * sz_pt, sz_pt)
                    # if point_in_tri(
                    #     mouse.world_point // size // 0.5 * 0.5,
                    #     sphere[ix[0]] * 1.15,
                    #     sphere[ix[1]] * 1.15,
                    #     sphere[ix[2]] * 1.15
                    # ):
                    #     print(f"Sector {rx}")
                    dist, _ = point_triangle_distance_Vec3(
                        (sphere[ix[0]] * size,
                         sphere[ix[1]] * size,
                         sphere[ix[2]] * size),
                        mouse.world_point
                    )
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_sector = rx

                sector = min_dist_sector

            buttons.append(Button(
                parent=scene,
                model=create_triangle_mesh(
                    sphere[i[0]] * 1.1,
                    sphere[i[1]] * 1.1,
                    sphere[i[2]] * 1.1
                ),
                scale=size,
                color=color.black66 if r % 4 < 2 else color.black50,
                on_click=callr,
                on_mouse_enter=do_nothing,
                on_mouse_exit=do_nothing,
            ))

    terrain = Entity(
        model=Mesh(
            vertices=z,
            triangles=mesh_.triangles,
            uvs=mesh_.uvs,
            normals=mesh_.normals,
            colors=col
        ),
        scale=size
    )

    ocean = Entity(
        model=Mesh(
            vertices=sphere,
            triangles=mesh_.triangles,
            uvs=mesh_.uvs,
            normals=mesh_.normals
        ),
        scale=size + 0.1,
        color=color.rgba(145, 120, 65, 150)
    )

    return terrain, ocean, buttons, sector


if __name__ == '__main__':
    app = Ursina()
    create_planet(30)
    EditorCamera()
    app.run()
