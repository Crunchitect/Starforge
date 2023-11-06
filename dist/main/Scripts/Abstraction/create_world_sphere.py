def run():
    e = earth()
    v = venus()
    v[0].x = 200
    v[1].x = 200
    for i in v[2]:
        i.x = 200
    return e, v


def earth():
    from Scripts.Proc.WorldGen.Planets.Earth.world_sphere import create_planet
    return create_planet(30)


def venus():
    from Scripts.Proc.WorldGen.Planets.Venus.world_sphere import create_planet
    return create_planet(30)


# def read_sector():
#     print(sector)
#     return sector
