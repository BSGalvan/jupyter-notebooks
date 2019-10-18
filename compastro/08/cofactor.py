#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:41:05 2019

@author: bsgalvan98
"""

import numpy as np

def cofactor(A, m, n):
    shape = np.shape(A)
    newshape = (shape[0]-1, shape[1]-1)
    B = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if(i != m and j != n):
                B.append(A[i][j])
    return np.reshape(B, newshape)