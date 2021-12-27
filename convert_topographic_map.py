from __future__ import with_statement 
from PIL import Image 
from collections import OrderedDict
import os

input_file = './topographic_map.jpg'
rgb_file = './output/rgb_values.csv'
topography_file = './output/topographic_plots.csv'
map_file = './output/map_plot_data.txt'

image = Image.open(input_file) 
 
# load the pixel info
pixels = image.load()
 
# get a tuple of the x and y dimensions of the image 
width, height = image.size 

# extract data about each pixel
tiles = OrderedDict()
for x in range(width): 
    for y in range(height): 
      r = pixels[x,y][0]
      g = pixels[x,y][1]
      b = pixels[x,y][2]
      if (b > 210):
        plotType=3 # ocean
        terrainType='TERRAIN_COAST'
      elif (r > 210 and g < 160):
        plotType=0 # mountain
        terrainType='TERRAIN_GRASS'
      elif (r > 160 and g > 160):
        plotType=1 # hill
        terrainType='TERRAIN_GRASS'
      else:
        plotType=2 # grassland
        terrainType='TERRAIN_GRASS'
      key = str(x) + '|' + str(height-y-1)
      tiles[key] = {'x': x, 'y': height-y-1, 'r': r, 'g': g, 'b': b, 'plot': plotType, 'terrain': terrainType}
 
# save each pixel's RGB data to a file
if (os.path.exists(rgb_file) and os.path.isfile(rgb_file)):
  os.remove(rgb_file)
  print(rgb_file + ' file deleted')
with open(rgb_file, 'w+') as file: 
  file.write('X,Y,R,G,B\n') 
  for key, value in tiles.items():
    tile = value
    file.write('{0},{1},{2},{3},{4}\n'.format(tile['x'],tile['y'],tile['r'],tile['g'],tile['b']))
print('Wrote file\'s RGG values to ' + rgb_file)

# save each pixel's terrain data to a file
if (os.path.exists(map_file) and os.path.isfile(map_file)):
  os.remove(map_file)
  print(map_file + ' file deleted')
with open(map_file, 'w+') as file: 
  file.write('### Plot Info ###')
  for key, value in tiles.items():
    tile = value
    file.write('\nBeginPlot\n\tx={0},y={1}\n\tTerrainType={2}\n\tPlotType={3}\nEndPlot'.format(tile['x'],tile['y'],tile['terrain'], tile['plot']))
print('Created map file with plot-types: ' + map_file)