directions = input()

directions = directions.split(', ')
distance = [0] * 2
horizontal = False
direction = True
places = set()

for step in directions:
    horizontal = not horizontal
    if step[0] == 'R':
        if not horizontal:
            direction = not direction
    else:
        if horizontal:
            direction = not direction

    sign = int(step[1:])
    for point in range(sign):
        if not direction:
            point = -1
        else:
            point = 1

        distance[0 if horizontal else 1] += point
        if tuple(distance) in places:
            print(abs(distance[0]) + abs(distance[1]), end=', ')
        places.add(tuple(distance))
