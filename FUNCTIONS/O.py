def major(x, y, z):
    return [x, y, z].count(1) > [x, y, z].count(0)

print(major(False, True, False))
