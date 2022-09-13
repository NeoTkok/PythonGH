commands = 'FFFFFLFFFLFFFFRRRFXFFFFFFS'
x, y = 0, 0
dx, dy = 1, 0

locs = [(0, 0)]
for cmd in commands:
    if cmd == 'S':
        break
    if cmd == 'F':
        x += dx
        y += dy
        if (x, y) in locs:
           print('Path crosses itself at: ({}, {})'.format(x, y))
        locs.append((x, y))
        continue
    if cmd == 'L':
        dx, dy = -dy, dx
        continue
    if cmd == 'R':
        dx, dy = dy, -dx
        continue
        print('Unknown command:', cmd)
    else:
        print('Instructions ended without a STOP')
x, y = zip(*locs)
xmin , xmax = min(x), max(x)
ymin , ymax = min(y), max(y)
nx = xmax - xmin + 1
ny = ymax - ymin + 1
for iy in reversed(range(ny)):
    for ix in range(nx):
        if (ix + xmin , iy + ymin) in locs:
            print('*', end='')
        else:
            print(' ', end='')
    print()
