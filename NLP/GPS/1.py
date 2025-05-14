import csv
from gmplot import gmplot

# Initialize empty lists
latitudes = []
longitudes = []

# Read from CSV
with open('C:/python/GPS/route_200.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        latitudes.append(float(row[0]))
        longitudes.append(float(row[1]))

# Initialize map at the first coordinate
gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 18)

# Plot the route in red
gmap.plot(latitudes, longitudes, color='red', edge_width=2.5)

# Optionally add a start and end marker
gmap.marker(latitudes[0], longitudes[0], color='green')  # Start point
gmap.marker(latitudes[-1], longitudes[-1], color='blue')  # End point

# Save the map
gmap.draw("C:/python/GPS/route_map.html")
print("Map has been saved to C:/python/GPS/route_map.html")
