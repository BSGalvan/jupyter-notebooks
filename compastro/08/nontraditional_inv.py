#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:45:04 2019

@author: bsgalvan98
"""

import numpy as np

def nontraditional_matrix_inverse(A):
    shape = np.shape(A)
    I = np.eye(shape[0])
    inv = np.zeros_like(A, dtype=float)
    for j in range(shape[1]):
        a = A
        b = I[:][j]
        inv[:][j] = np.linalg.solve(a, b)
    return inv.T