def c_roi(velocity, threshold, x_layer, y_layer, l_array):
    import math
    import matplotlib.pyplot as plt
    import numpy as np
    # import h5py

    r = 0
    t_roi = 0
    vel = velocity
    stp = threshold

    cor_x = []
    cor_y = []
    cor_ax = []
    cor_ay = []
    sub_plot_x = []
    sub_plot_y = []
    rd_lyr = []
    x_sbplt = []
    y_sbplt = []
    roi_data = []
    roi_data_l = []
    roi_d = [0, 0]
    roi = []
    t = []

    for n in range(len(l_array)):
        min_x = min(x_layer[n])
        min_y = min(y_layer[n])

        cor_x = []
        cor_y = []

        for m in range(len(l_array[n])):
            if (min_x < 0):
                x_c = x_layer[n][m] - min_x
            else:
                x_c = x_layer[n][m]
            if (min_y < 0):
                y_c = y_layer[n][m] - min_y
            else:
                y_c = y_layer[n][m]

            cor_x.append(x_c)
            cor_y.append(y_c)

        cor_ax.append(cor_x)
        cor_ay.append(cor_y)

    for i in range(len(l_array)):
        for j in range(len(l_array[i])):
            if j == 0 and i != 0:
                x_0 = cor_ax[i - 1][len(l_array[i - 1]) - 1]
                x_f = cor_ax[i][j]

                y_0 = cor_ay[i - 1][len(l_array[i - 1]) - 1]
                y_f = cor_ay[i][j]

            else:
                x_0 = cor_ax[i][j - 1]
                x_f = cor_ax[i][j]

                y_0 = cor_ay[i][j - 1]
                y_f = cor_ay[i][j]

            vec = [x_f - x_0, y_f - y_0]

            x_sq = pow(vec[0], 2)
            y_sq = pow(vec[1], 2)

            mag = math.sqrt(x_sq + y_sq)

            if mag != 0:
                unit_vec = [vec[0] / mag, vec[1] / mag]

            if mag > stp:
                dist = int((mag + r) / stp)
                r = (mag + r) % stp
                x_d = x_0
                y_d = y_0
                roi_d = [x_d, y_d]

                for d in range(dist + 1):
                    roi_Vec = [x_d - x_0, y_d - y_0]
                    x_rsq = pow(roi_Vec[0], 2)
                    y_rsq = pow(roi_Vec[1], 2)

                    mag_roi = math.sqrt(x_rsq + y_rsq)

                    t_roi += mag_roi / vel

                    if mag_roi < mag:
                        t.append(t_roi)
                        roi.append(roi_d)
                        sub_plot_x.append(x_d)
                        sub_plot_y.append(y_d)
                        data = [x_d, y_d, unit_vec[0], unit_vec[1], t_roi]
                        data_l = [x_d, y_d, unit_vec[0], unit_vec[1], t_roi, i + 1]
                        roi_data.append(data)
                        roi_data_l.append(data_l)
                        x_d += stp * unit_vec[0]
                        y_d += stp * unit_vec[1]
                        roi_d = [x_d, y_d]

                    if mag < stp:
                        if r < stp:
                            r += mag
                            t_roi += r / vel
                        if r >= stp:
                            t.append(t_roi)
                            roi_d = [x_f, y_f]
                            roi.append(roi_d)
                            sub_plot_x.append(roi_d[0])
                            sub_plot_y.append(roi_d[1])
                            data = [x_d, y_d, unit_vec[0], unit_vec[1], t_roi]
                            data_l = [x_d, y_d, unit_vec[0], unit_vec[1], t_roi, i + 1]
                            r = 0
                            roi_data.append(data)
                            roi_data_l.append(data_l)
        x_sbplt.append(sub_plot_x)
        y_sbplt.append(sub_plot_y)
        sub_plot_x = []
        sub_plot_y = []
        rd_lyr.append(roi_data)

    data_arr = np.array(roi_data_l)
    list_data = [cor_ax, cor_ay, x_sbplt, y_sbplt]

    return data_arr, list_data
