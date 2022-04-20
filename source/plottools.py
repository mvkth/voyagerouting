from source.geotools import PH
import matplotlib.pyplot as plt

class PlotTools:
    @staticmethod
    def plot_segment(a, b, c='#3ea3b0'):
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay
        plt.arrow(ax, ay, dx, dy, width=0.0005,color=c)

    @staticmethod
    def showPlot():
        plt.show()

    @staticmethod
    def plotPH():
        PH.plot(color='green')

    @staticmethod
    def plotEdges(edges):
        for orig, neighbors in edges.items():
            for dest in neighbors.values():
                PlotTools.plot_segment(orig, dest)
    
    @staticmethod
    def plotPoints(points):
        for row in points:
            for col in row:
                if col:
                    x, y = col
                    plt.scatter(x, y, s=3, c='blue')