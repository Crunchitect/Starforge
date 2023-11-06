from Scripts.Proc.WorldGen.Planets.Earth.world_plane import create_world
from ursina import deepcopy, Vec3, Mesh, MeshCollider, color


def run():
    t, o = create_world(100)
    t.collider = 'mesh'
    t.collision = True

    for i in range(1):
        for j in range(1):
            ti, oi = deepcopy((t, o))
            ti_v, oi_v = [], []
            for k in t.model.vertices:
                ti_v.append(Vec3(k.x+i, k.y, k.z+j))
            for k in o.model.vertices:
                oi_v.append(Vec3(k.x + i, k.y, k.z + j))
            ti.model = Mesh(
                vertices=ti_v,
                triangles=t.model.triangles,
                uvs=t.model.uvs,
                normals=t.model.normals,
                colors=t.model.colors,
            )
            oi.model = Mesh(
                vertices=oi_v,
                triangles=o.model.triangles,
                uvs=o.model.uvs,
                normals=o.model.normals,
                colors=color.rgba(0, 157, 196, 150),
            )
            ti.collider = MeshCollider(ti, mesh=ti.model, center=Vec3(0, -5000, 0))
            ti.collision = True
            return ti, oi
