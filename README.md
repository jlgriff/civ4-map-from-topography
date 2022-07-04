# Introduction

This application converts typical topgraphic maps into plot data that can be used to build maps for the video game Civilization IV.

# Selecting a Map

Overwrite the `topographic_map.jpg` file with the topographic map .jpg that you wish to convert.

Included is a `example_topographic_map.jpg` of Britain that can be used for reference.

### Colors

The script interprets red as mountains, yellow as hills, and green as plains when it's converting to Civ4 plot data.

### Size

It also creates a tile for each pixel, so it's important to degrade the resolution of your image appropriately. (That way, it doesn't take your warrior taking 750 years to cross the map.) You'll notice that the included Britain map is 128x85 pixels.

## Aspect Ratio

One last thing: a Civ4 map must follow one of the allowed aspect ratios in order to load. It doesn't have to be one of these sizes, but must follow the same ratio. These aspect ratios are as follows:
 1. 40x24   (5x3)
 2. 52x32   (13x8)
 3. 64x40   (8x5)
 4. 80x48   (5x3)
 5. 100x60  (5x3)
 6. 128x80  (8x5)
 7. 160x100 (8x5)

# Create Plot Data

Generate the plot data and save it to a generated `output` directory with either of the following commands.

### If using Python

1. Run `python convert_topographic_map.py`.

### If using Docker

1. Run `docker build -t civ4-map-from-topography .`.
2. Run `docker run -it --rm --name civ4-map-from-topography -v "/$(pwd)/output:/src/output" civ4-map-from-topography` on Mac, or `docker run -it --rm --name civ4-map-from-topography -v "C:\Users\<user>\git\civ4-map-from-topography\output:/src/output" civ4-map-from-topography` on Windows (replacing `<user>` with your root user).
