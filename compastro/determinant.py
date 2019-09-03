#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:27:18 2019

@author: bsgalvan98
"""

import numpy as np
from cofactor import cofactor

def determinant(A):
    shape = np.shape(A)
    result = 0.
    if(shape[0] == 2):
        result = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    else:
        for j in range(shape[1]):
            term = 1.
            term *= ((-1.)**j)*A[0][j]
            cofactor_matrix = cofactor(A, 0, j)
            term *= determinant(cofactor_matrix)
            result += term
    return result
        
        
    

