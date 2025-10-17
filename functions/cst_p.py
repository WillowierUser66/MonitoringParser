def cst_parser(filepathname):
    import re
    import math

    global sub_list
    global parent_list
    global plot_x
    global plot_y
    # global plot_num

    i = 0
    g = 0
    x = 0
    y = 0
    p = 0

    sub_list = [[0 for n in range(5)] for n in range(1)]
    parent_list = []
    plot_x = []
    plot_y = []
    plot_num = []

    with open(filepathname, 'r') as gcode:

        for line in gcode:

            line = line.strip()
            coord = re.findall(r'[XY].?\d+.\d+|[XY].?\d+.', line)
            dep = re.findall(r'DEPOSITION', line)
            layer = re.findall(r'Layer Number', line)
            line_c = re.findall(r'[N].?\d+', line)
            g_0 = re.findall(r'G0', line)

            if layer:
                i += 1
                # print("Layer",i)
            if g_0:
                g = 0
            else:
                g = 1
            if dep:
                p += 1
            if coord:
                # line_Num = line_c[0].replace('N','')
                # Num = int(line_Num)
                # print(line_Num)
                if len(coord) == 1:
                    if 'Y' in coord[0]:
                        x = x
                        y_s = coord[0].replace('Y', '')
                        y = float(y_s)
                    if 'X' in coord[0]:
                        x_s = coord[0].replace('X', '')
                        x = float(x_s)
                        y = y
                else:
                    x_s = coord[0].replace('X', '')
                    y_s = coord[1].replace('Y', '')
                    x = float(x_s)
                    y = float(y_s)
                sub_list = (g, x, y, i)
                plot_x.append(x)
                plot_y.append(y)
                # plot_num.append(Num)
                parent_list.append(sub_list)
    # print(parent_list)
    # print(plot_x, plot_y)
    # returns x array, y array and complete list
    return plot_x, plot_y, parent_list


