#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:15:39 2019

@author: bsgalvan98
"""

import numpy as np
from determinant import determinant
from cofactor import cofactor

def traditional_matrix_inverse(A):
    delta = determinant(A)
    shape = np.shape(A)
    adj = np.zeros_like(A)
    for i in range(shape[0]):
        for j in range(shape[1]):
            adj[i][j] = (-1.)**(i + j) * determinant(cofactor(A, i, j))
    adj = adj.T
    inv = np.power(delta, -1) * adj
    return inv