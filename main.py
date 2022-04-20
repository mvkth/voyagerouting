from source.geotools import GeoTools
from source.plottools import PlotTools
from source.nodemap import NodeMap
from source.graphtools import Graph, Path
from source.weathertools import WeatherTools, driver

points = GeoTools.filterWater(GeoTools.makeMatrix(step=0.25))
neighbors = GeoTools.getNeighbors(points)
weather = WeatherTools.getWeather(points)

nodes = NodeMap.generate_nodes(points, neighbors, weather)
# NodeMap.show_nodes(nodes)

graph = Graph(nodes)
# graph.show_edges()
paths = graph.dijkstra(points[0][0])

PlotTools.plotPH()
PlotTools.plotEdges(neighbors)
PlotTools.plotPoints(points)

path = Path.generate_path(paths,(122.0, 12.0))
for i in path:
    a , b = i
    PlotTools.plot_segment(a,b,'#ffbb00')

PlotTools.set_xlim(119,123)
PlotTools.set_ylim(9.5,13.0)
PlotTools.showPlot()
driver.quit()