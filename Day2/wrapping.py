import csv

# Parse Data
data = []
with open('./dimensions.txt', 'r') as csv_data:
  # Pull in raw data as strings in a list.
    csvreader = csv.reader(csv_data, delimiter='x')
      #data = [int(value) for value in next(csv_data).split(',')]
    for row in csvreader:
        data.append([int(value) for value in row])
# for row in data:
#     data[row] = [int(value) for value in row]

# order is: L, W, H
#  side a = L * W 
#  side b = W * H 
#  side c = H * L
# surface area = 2*l*w + 2*w*h + 2*h*l
# + area of smallest side
def partOne():
    totalPaper = 0
    for i,row in enumerate(data):
        sideA = 0
        sideB = 0
        sideC = 0
        smol = 0
        area = 0

        sideA = data[i][0]*data[i][1]
        sideB = data[i][1]*data[i][2]
        sideC = data[i][2]*data[i][0]
        smol = min(sideA, sideB, sideC)
        area = 2*sideA + 2*sideB + 2*sideC + smol
        totalPaper = totalPaper + area


    print(totalPaper)

def partTwo():
    # bow = cubic feet of vol of present
    totalRibbon = 0
    for i,row in enumerate(data):
        bow = 0
        ignore = 0

        ignore = max(data[i][0], data[i][1], data[i][2])
        ribbon = (data[i][0]*2 + data[i][1]*2 + data[i][2]*2) - ignore*2
        bow = (data[i][0]*data[i][1]*data[i][2])
        totalRibbon = totalRibbon + ribbon + bow
    print(totalRibbon)


partTwo()
