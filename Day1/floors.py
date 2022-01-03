# Parse Data
data = []
with open('./directions.txt') as csv_data:
  # Pull in raw data as strings in a list.
  data = [val for val in next(csv_data)]

def partOne():
    # ( means go up a floor, ) means go down a floor
    floor = 0

    for i in data:
        if i == '(':
            floor = floor + 1
        elif i == ')':
            floor = floor - 1


    print(floor)

def partTwo():
    floor = 0
    basement = 0
    for index,i in enumerate(data):
        if i == '(':
            floor = floor + 1
        elif i == ')':
            floor = floor - 1
            if floor < 0:
                basement = index + 1
                break
    print(basement)

    # 3883 is too high
    print(floor)

partTwo()