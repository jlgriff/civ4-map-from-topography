from __future__ import with_statement 
from PIL import Image 
from collections import OrderedDict
import numpy as np
import os

inputFile = './topographic_map.jpg'
rgbFile = './output/rgb_values.csv'
plotDataFile = './output/map_plot_data.txt'
coastDistanceFromLand = 4

image = Image.open(inputFile) 
 
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
      if (b > 205):
        plotType=3 # ocean
        terrainType='TERRAIN_OCEAN'
        feature=None
        featureVariety=0
      elif (r > 210 and g < 160):
        plotType=0 # mountain
        terrainType='TERRAIN_GRASS'
        feature=None
        featureVariety=0
      elif (r > 160 and g > 160):
        plotType=1 # hill
        terrainType='TERRAIN_GRASS'
        feature=None
        featureVariety=0
      else:
        plotType=2 # grassland
        terrainType='TERRAIN_GRASS'
        feature=None
        featureVariety=0
      key = str(x) + '|' + str(height-y-1)
      tiles[key] = {'x': x, 'y': height-y-1, 'r': r, 'g': g, 'b': b, 'plot': plotType, 'terrain': terrainType, 'feature': feature, 'featureVariety': featureVariety}

# Determine whether terrain should be ocean or coast by its proximity to land plots
coastalRange = np.arange(-coastDistanceFromLand, coastDistanceFromLand + 1, 1)
for key, value in tiles.items():
  if (value['plot'] == 3):
    x = value['x']
    y = value['y']
    for adjacentX in coastalRange:
      for adjacentY in coastalRange:
        key = str(x + adjacentX) + '|' + str(y + adjacentY)
        if (key in tiles 
        and (abs(adjacentX) != coastDistanceFromLand and abs(adjacentY) != coastDistanceFromLand)): # Ensuring that both X and Y aren't both max distance prevents a blocky look
          adjacentTile = tiles[key]
          if (adjacentTile['plot'] == 0 or adjacentTile['plot'] == 1 or adjacentTile['plot'] == 2):
            value['terrain'] = 'TERRAIN_COAST'
 
# save each pixel's RGB data to a file
if (os.path.exists(rgbFile) and os.path.isfile(rgbFile)):
  os.remove(rgbFile)
  print(rgbFile + ' file deleted')
with open(rgbFile, 'w+') as file: 
  file.write('X,Y,R,G,B\n') 
  for key, tile in tiles.items():
    file.write('{0},{1},{2},{3},{4}\n'.format(tile['x'],tile['y'],tile['r'],tile['g'],tile['b']))
print('Wrote file\'s RGG values to ' + rgbFile)

# save each pixel's terrain data to a file
if (os.path.exists(plotDataFile) and os.path.isfile(plotDataFile)):
  os.remove(plotDataFile)
  print(plotDataFile + ' file deleted')
with open(plotDataFile, 'w+') as file: 
  file.write('### Plot Info ###')
  for key, tile in tiles.items():
    file.write('\nBeginPlot\n\tx={0},y={1}\n\tTerrainType={2}\n\tPlotType={3}'.format(tile['x'],tile['y'],tile['terrain'], tile['plot']))
    if (tile['feature'] is not None):
      file.write('\n\tFeatureType={0}\n\tFeatureVariety={1}'.format(tile['feature'],tile['featureVariety']))
    file.write('\nEndPlot')
print('Created map file with plot-types: ' + plotDataFile)