def ornl_parser(filepathname):
    import re
    import matplotlib.pyplot as plt
    import numpy as np
    # import h5py

    global l_array
    global x_layer
    global y_layer

    l_array = []
    x_layer = []
    y_layer = []
    pre_x = []
    pre_y = []
    points = []

    with open(filepathname, 'r') as gcode:
        for line in gcode:

            line = line.strip()
            coord = re.findall(r'[XY].?\d+.\d+|[XY].?\d+.', line)
            layers_str = re.findall(r'LAYER COUNT: .?\d+', line)
            lyr = re.findall(r'(BEGINNING LAYER: \d+)', line)
            if layers_str:
                lyrs_str = layers_str[0].replace('LAYER COUNT: ', '')
                layers = float(lyrs_str)

            if coord:

                if len(coord) == 1:
                    if 'Y' in coord[0]:
                        y_s = coord[0].replace('Y', '')
                        y = float(y_s)
                        y = y - 9.5
                    if 'X' in coord[0]:
                        x_s = coord[0].replace('X', '')
                        x = float(x_s)
                        x = x - 18
                else:
                    x_s = coord[0].replace('X', '')
                    y_s = coord[1].replace('Y', '')
                    x = float(x_s) - 18
                    y = float(y_s) - 9.5
                pre_x.append(x)
                pre_y.append(y)
                points.append([x, y])

            if lyr:
                l_array.append(points)
                x_layer.append(pre_x)
                y_layer.append(pre_y)
                points = []
                pre_x = []
                pre_y = []

    l_array.pop(0)
    x_layer.pop(0)
    y_layer.pop(0)

    return x_layer, y_layer, l_array
# print(parent_list)

