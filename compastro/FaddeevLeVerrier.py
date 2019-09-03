#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:38:47 2019

@author: bsgalvan98
"""

import numpy as np

def FLV(A):
    n = np.shape(A)[0]
    c = np.zeros(n + 1)
    I = np.eye(n)
    for k in range(n + 1):
        if(k == 0):
            M = np.zeros_like(A, dtype=float)
            c[-1] = 1.
        else:
            M = np.matmul(A, M) + c[n - k + 1] * I
            c[n - k] = (-1 / k) * np.trace(np.matmul(A, M))
    inv = (-1 / c[0]) * M
    print(c)
    return inv