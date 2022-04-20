# map libraries
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, LineString
# path libraries
from pathlib import Path
# get portable filepath
FILE_PATH = Path.cwd() / 'data' / 'shape' / 'phl.shp'
FILE_PATH = FILE_PATH.resolve()
# default parameters for grid
LATITUDE = (110.0, 125.5)
LONGITUDE = (5.0, 20.5)
STEP = 1.0
# open shape file
try:
    PH = gpd.read_file(FILE_PATH)
except exception as Exception:
    print(exception)

def get_relative_direction(A):
    x, y = A
    if(x == 0 and y == 1):
        return 'north'
    if(x == 0 and y == -1):
        return 'south'
    if(x == 1 and y == 0):
        return 'east'
    if(x == -1 and y == 0):
        return 'west'
    if(x == 1 and y == 1):
        return 'eastnorth'
    if(x == 1 and y == -1):
        return 'eastsouth'
    if(x == -1 and y == 1):
        return 'westnorth'
    if(x == -1 and y == -1):
        return 'westsouth'

class GeoTools:
    @staticmethod
    def makeMatrix(longitude=None, latitude=None, step=None):
        if not longitude:
            longitude = LONGITUDE
        if not latitude:
            latitude = LATITUDE
        if not step:
            step = STEP
        min_y, max_y = longitude
        min_x, max_x = latitude
        lon = np.arange(min_y, max_y, step)
        lat = np.arange(min_x, max_x, step)
        length = lon.size
        width = lat.size
        lon, lat = np.meshgrid(lat, lon)
        points = list(zip(lon.flatten(), lat.flatten()))
        matrix = np.array(points,dtype='f,f').reshape(length, width).T.tolist()
        return matrix

    @staticmethod
    def filterWater(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                p = Point(matrix[i][j])
                if (PH.contains(Point(p)).bool()):
                    matrix[i][j] = None
        return matrix

    @staticmethod
    def getNeighbors(matrix):
        # returns dictionary where KEY is position, and VALUE is dictionary of neighbors
        # neighbors is a dictionary where KEY is cardinal direction and VALUE is position of neighbor
        position = {}
        rows = range(len(matrix))
        for i in rows:
            cols = range(len(matrix[i]))
            for j in cols:
                if matrix[i][j] is not None:
                    x, y = matrix[i][j]
                    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
                    neighbors = {}
                    for direction in directions:
                        dx, dy = direction
                        if((i+dx) in rows and (j+dy) in cols):
                            endPoint = matrix[i+dx][j+dy]
                            if endPoint is not None:
                                segment = LineString([(x,y), endPoint])
                                if not PH.crosses(segment).bool():
                                    relDir = get_relative_direction(direction)
                                    neighbors[relDir] = endPoint
                    position[matrix[i][j]] = neighbors
        return position