# -*- coding: utf-8 -*-
'''calc absorbance'''
import numpy as np


def calc_abs(file_path):
    '''path = [ts_m, bg_m, ts_r, bg_r]
    ts_m -> Transmission spectrum of material
    bg_m -> Back ground spectrum of material
    ts_r -> Transmission spectrum of reference
    bg_r -> Back ground spectrum of reference
    '''
    ts_m_data = np.loadtxt(file_path[0], dtype='float')
    bg_m_data = np.loadtxt(file_path[1], dtype='float')
    ts_r_data = np.loadtxt(file_path[2], dtype='float')
    bg_r_data = np.loadtxt(file_path[3], dtype='float')

    temp_y = -np.log10((ts_m_data[:, 1:2] - bg_m_data[:, 1:2]) /
                       (ts_r_data[:, 1:2] - bg_r_data[:, 1:2]))
    print(temp_y)

    return np.concatenate([ts_m_data[:, 0:1], temp_y], 1)
