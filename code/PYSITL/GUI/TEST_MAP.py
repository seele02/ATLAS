import gmplot

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

longitudes = [-122.145, -122.145, -122.145, -122.146, -122.146]
latitudes = [37.429, 37.428, 37.427, 37.427, 37.427]

gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
#gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")