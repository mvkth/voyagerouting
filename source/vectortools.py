import math

DISTANCE_FACTOR = 110.574

CARD_TO_DEG = {
    'north' : 90.0,
    'east' : 0.0,
    'south' : 270.0,
    'west' : 180.0,
    'eastnorth' : 45.0,
    'eastsouth' : 315.0,
    'westnorth' : 135.0,
    'westsouth' : 225.0
}

PROJECTION_ANGLES = {
    'eastnorth' : 45.0,
    'westnorth' : -45.0,
    'eastsouth' : 135.0,
    'westsouth' : -135.0
}

def angle(VECTOR):
    # A is tuple of vector components (x,y)
    x, y = VECTOR
    return math.degrees(math.atan2(y,x))

def magnitude(VECTOR):
    x, y = VECTOR
    return math.sqrt((x*x) + (y*y))

def cartesian(VECTOR):
    angle, magnitude = VECTOR
    x = math.cos(math.radians(angle))*magnitude
    y = math.sin(math.radians(angle))*magnitude
    return (x,y)

def diagonal(A, B):
    Ax, Ay = A
    Bx, By = B
    Rx, Ry = (Bx - Ax), (By - Ay)
    return math.sqrt((Rx*Rx) + (Ry*Ry))

def sum_cartesian(A, B):
    Ax, Ay = A
    Bx, By = B
    Rx, Ry = (Ax + Bx), (Ay + By)
    return (Rx, Ry)

class VectorTools:
    @staticmethod
    def sum_current(A, B):
        if A:
            Ax, Ay = cartesian(A)
        else:
            Ax, Ay = 0, 0
        if B:
            Bx, By = cartesian(B)
        else:
            Bx, By = 0, 0
        R = sum_cartesian((Ax, Ay), (Bx, By))
        return (angle(R), magnitude(R))

    @staticmethod
    def sum_height(A, B):
        R = []
        if(A):
            R.append(A)
        if(B):
            R.append(B)
        return (sum(R)/2)

    @staticmethod
    def distance(A, B):
        return diagonal(A, B) * DISTANCE_FACTOR

    @staticmethod
    def delta(current, direction, height):
        angle, magnitude = current
        if direction in PROJECTION_ANGLES.keys():
            offset = PROJECTION_ANGLES[direction]
            result = math.sin(math.radians(angle + offset)) * magnitude * height * height * 3.60
        else:
            result = math.sin(math.radians(angle)) * magnitude * height * height * 3.60
            if direction in ['south','west']:
                result = (-1) * result
        return result