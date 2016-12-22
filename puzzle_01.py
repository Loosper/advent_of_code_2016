directions = input()

directions = directions.split(', ')
distance = [0] * 2
horizontal = False
direction = True

for step in directions:
    horizontal = not horizontal
    if step[0] == 'R':
        if not horizontal:
            direction = not direction
    else:
        if horizontal:
            direction = not direction

    sign = int(step[1:])
    if not direction:
        sign *= -1

    distance[0 if horizontal else 1] += sign


print(distance[0] + distance[1])
