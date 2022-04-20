from source.geotools import GeoTools
from source.plottools import PlotTools
from source.nodemap import NodeMap
from source.graphtools import Graph, Path
from source.weathertools import WeatherTools, driver

points = GeoTools.filterWater(GeoTools.makeMatrix(step=2.0))
neighbors = GeoTools.getNeighbors(points)
weather = WeatherTools.getWeather(points)

nodes = NodeMap.generate_nodes(points, neighbors, weather)
# NodeMap.show_nodes(nodes)

PlotTools.plotPH()
PlotTools.plotEdges(neighbors)
PlotTools.plotPoints(points)
PlotTools.showPlot()

graph = Graph(nodes)
# graph.show_edges()
paths = graph.dijkstra(points[0][0])
path = Path.generate_path(paths,(124.0, 9.0))
for i in path:
    a , b = i
    PlotTools.plot_segment(a,b,'#ffbb00')
driver.quit()