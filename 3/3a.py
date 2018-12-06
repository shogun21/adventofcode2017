n = input("Enter number to get coordinate: ")

def coordinate(num):
    x = 0
    y = 0
    maxXY = 0
    vX = 1
    vY = 0
    for i in range(1, int(num) + 1):
        
        print (str(i) + " (" + str(x) + "," + str(y) + ")" + " maxXY: " + str(maxXY) + " vX: " + str(vX) + " vY: " + str(vY))

        x += vX
        y += vY
        
        if (y == maxXY and x == maxXY):
            vX = -1
            vY = 0
        elif (y == maxXY and x == -maxXY):
            vX = 0
            vY = -1
        elif (y == -maxXY and x == maxXY):
            vX = 0
            vY = 1
        elif (y == -maxXY and x == -maxXY):
            vX = 1
            vY = 0

        if (x > maxXY):
            maxXY += 1


coordinate(n)
