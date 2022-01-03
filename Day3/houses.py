# Parse Data
data = []
with open('./directions.txt') as csv_data:
  # Pull in raw data as strings in a list.
  data = [val for val in next(csv_data)]


# starting pos: x = 0, y = 0
# > = move right // x += 1
# < = move left // x -= 1
# ^ = move up // y += 1
# v = move down // y -= 1

# for every value in data, which way do we move,
#   append the new pos to posTable
# find distinct in the list. unique

def partOne():
    x = 0
    y = 0
    pos = [[0, 0]]
    houses = {}
    for i in data:
        if i == ">":
            x = x + 1
            y = y
            pos.append([x, y])
        if i == "<":
            x = x - 1
            y = y
            pos.append([x, y])
        if i == "^":
            x = x
            y = y + 1
            pos.append([x, y])
        if i == "v":
            x = x
            y = y - 1
            pos.append([x, y])
    # pos_set = set(pos)
    # houses = len(pos_set)
    for i in pos:
        houses.setdefault(tuple(i), list().append(1))

    print(len(houses))

def partTwo():
    houses = {}
    x = 0
    y = 0
    santaPos = [[0, 0]]
    rx = 0
    ry = 0
    roboPos = [[0, 0]]

    for index,i in enumerate(data):
        if index % 2 == 0:
            if i == ">":
                x = x + 1
                y = y
                santaPos.append([x, y])
            if i == "<":
                x = x - 1
                y = y
                santaPos.append([x, y])
            if i == "^":
                x = x
                y = y + 1
                santaPos.append([x, y])
            if i == "v":
                x = x
                y = y - 1
                santaPos.append([x, y])
        elif (index % 2) != 0:
            if i == ">":
                rx = rx + 1
                ry = ry
                roboPos.append([rx, ry])
            if i == "<":
                rx = rx - 1
                ry = ry
                roboPos.append([rx, ry])
            if i == "^":
                rx = rx
                ry = ry + 1
                roboPos.append([rx, ry])
            if i == "v":
                rx = rx
                ry = ry - 1
                roboPos.append([rx, ry])
    # pos_set = set(pos)
    # houses = len(pos_set)
    for i in santaPos:
        houses.setdefault(tuple(i), list().append(1))
    for i in roboPos:
        houses.setdefault(tuple(i), list().append(1))
    print(len(houses))
    # print(f"roboPos: {r}")
    # 3037 is too high

partTwo()