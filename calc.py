# -*- coding: utf-8 -*-
'''calc absorbance'''
import csv
import numpy as np


def file_opener(file_path):
    '''tsv or csv opened and return x,y parameter'''
    f_1 = open(file_path, 'r')
    if('.csv' in file_path):
        f_1 = open(file_path, 'r')
    f1list = list(csv.reader(f_1, delimiter='\t'))
    x_list = []
    y_list = []
    for i in f1list:
        x_list.append(float(i[0]))
        y_list.append(float(i[1]))
    return x_list, y_list


def calc_abs(file_path):
    '''path = [ts_m, bg_m, ts_r, bg_r]
    ts_m -> Transmission spectrum of material
    bg_m -> Back ground spectrum of material
    ts_r -> Transmission spectrum of reference
    bg_r -> Back ground spectrum of reference
    '''
    ts_m_data = file_opener(file_path[0])
    bg_m_data = file_opener(file_path[1])
    ts_r_data = file_opener(file_path[2])
    bg_r_data = file_opener(file_path[3])

    output_x = []
    output_y = []
    for i, _ in enumerate(bg_m_data[0]):
        param = -np.log10((ts_m_data[1][i] - bg_m_data[1][i])/(
            ts_r_data[1][i] - bg_r_data[1][i]))
        output_x.append(bg_m_data[0][i])
        output_y.append(param)
    return output_x, output_y
