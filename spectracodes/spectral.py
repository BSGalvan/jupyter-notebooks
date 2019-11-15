#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:59:17 2019

@author: bharath
"""

#Imports and Auxiliary Functions
import numpy as np
from math import floor
import matplotlib.pyplot as plt

def move_forward(wavelength, start, end):
    if(end + steps > np.size(wavelength)):
        print("Cannot move forward! Already at the end!")
    else:
        start = end
        end = end + steps
    return(start, end)
        
def move_backward(wavelength, start, end):
    if(start - steps < 0):
        print("Cannot move backward! Already at the start!")
    else:
        end = start
        start = start - steps
    return(start, end)

def lamfluxrange(start, end, wavelength, flux):
    return(wavelength[start:end+1], flux[start:end+1])
    
#Getting data from the .txt file
lam, flux, flux_err, continuum = np.genfromtxt("PG1424_240_HST.txt", dtype=float, unpack=True)
delta_lam = lam[1] - lam[0]
cont_norm_flux = np.divide(flux, continuum)
steps = floor(40./delta_lam)
start_init = 0
end_init = start_init + steps

#Main plotting function
fig = plt.figure()
fig.set_size_inches(7.5,7.5)
wavelength_range, flux_range = lamfluxrange(start_init, end_init, lam, cont_norm_flux)
plt.plot(wavelength_range, flux_range, ds='steps')
plt.show()
cmd = input("Enter a command (d for forward, a for backward, h for halt): ")
start = start_init
end = end_init
while(cmd != "h"):
    if(cmd == 'd'):
        start, end = move_forward(lam, start, end)
        wavelength_range, flux_range = lamfluxrange(start, end, lam, cont_norm_flux)
        plt.close(fig)
        fig = plt.figure()
        fig.set_size_inches(7.5,7.5)
        plt.plot(wavelength_range, flux_range, ds='steps')
        plt.show()
    elif(cmd == 'a'):
        start, end = move_backward(lam, start, end)
        wavelength_range, flux_range = lamfluxrange(start, end, lam, cont_norm_flux)
        plt.close('all')
        fig = plt.figure()
        fig.set_size_inches(7.5,7.5)
        plt.plot(wavelength_range, flux_range, ds='steps')
        plt.show()
    else:
        print("Invalid character entered!")
    cmd = input("Enter a command (d for forward, a for backward, h for halt): ")