import random

# classes
class vector3:

    x = 0
    y = 0 
    z = 0

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class vector2:

    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

# barycentric triangle
def barycentric(pointA,pointB,pointC,position):

    # barycentric calculations
    det = (pointB.z - pointC.z) * (pointA.x - pointC.x) + (pointC.x - pointB.x) * (pointA.z - pointC.z)

    lineA = ((pointB.z - pointC.z) * (position.x - pointC.x) + (pointC.x - pointB.x) * (position.y - pointC.z))/det
    lineB = ((pointC.z - pointA.z) * (position.x - pointC.x) + (pointA.x - pointC.x) * (position.y - pointC.z))/det
    lineC = 1 - lineA - lineB

    # returning the found height
    y = lineA*pointA.y + lineB*pointB.y + lineC*pointC.y
    return y

def start():

    # quad points (square)
    points = [
        vector3(0,random.randint(1,10),1), # top left corner
        vector3(1,random.randint(1,10),1), # top right corner
        vector3(0,random.randint(1,10),0), # bottom left corner
        vector3(1,random.randint(1,10),0)  # bottom right corner
    ]

    # the position.y will act like the z coordinate
    position = vector2(random.random(),random.random())

    y = None
    if position.x < position.y:
        y = barycentric(points[0],points[1],points[2],position)
        print("x is smaller than y \n")

    else:
        y = barycentric(points[2],points[1],points[3],position)
        print("x is bigger than y \n")

    for coords in points:
        print("[COORDS]: x " + str(coords.x) + ", y " + str(coords.y) + ", z " + str(coords.z))
    print("\n[POSITION]: " + str(position.x) + " " + str(position.y))

    print("Y found: " + str(y))

start()
