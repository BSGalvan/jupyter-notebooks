#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:38:24 2019

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

def get_limits():
    start = np.float(input("Enter the start wavelength: "))
    end = np.float(input("Enter the end wavelength: "))
    return(start, end)

def eq_width(wavelength, flux, flux_err, lam_start, lam_end):
    delta_lam = wavelength[1]-wavelength[0]
    flux = flux[np.multiply(wavelength >= lam_start, wavelength <= lam_end)]
    flux_err = flux_err[np.multiply(wavelength >= lam_start, wavelength <= lam_end)]
    val = np.sum( (1 - flux) * delta_lam )
    error = np.sqrt( np.sum( np.power(flux_err, 2) ) )
    return val, error

def zeq_width(z, wavelength, flux, flux_err, lam_start, lam_end):
    delta_lam = wavelength[1]-wavelength[0]
    flux = flux[np.multiply(wavelength >= lam_start, wavelength <= lam_end)]
    flux_err = flux_err[np.multiply(wavelength >= lam_start, wavelength <= lam_end)]
    val = np.sum( (1 - flux) * delta_lam ) / (1 + z)
    error = np.sqrt( np.sum( np.power(flux_err, 2) ) ) / (1 + z)
    return val, error

#Getting data from the .txt file
lam, flux, flux_err, continuum = np.genfromtxt("PG1424_240_HST.txt", dtype=float, unpack=True)
delta_lam = lam[1] - lam[0]
cont_norm_flux = np.divide(flux, continuum)
cont_norm_flux_err = np.divide(flux_err, continuum)
steps = floor(40./delta_lam)
start_init = 0
end_init = start_init + steps

#Main plotting function
fig = plt.figure()
wavelength_range, flux_range = lamfluxrange(start_init, end_init, lam, cont_norm_flux)
plt.plot(wavelength_range, flux_range, ds='steps')
plt.show()
cmd = input("Enter a command (d for forward, a for backward, e for equivalent width, h for halt, z for redshift): ")

start = start_init
end = end_init
while(cmd != "h"):
    if(cmd == 'd'):
        start, end = move_forward(lam, start, end)
        wavelength_range, flux_range = lamfluxrange(start, end, lam, cont_norm_flux)
        plt.close('all')
        fig = plt.figure()
        plt.plot(wavelength_range, flux_range, ds='steps')
        plt.show()
    elif(cmd == 'a'):
        start, end = move_backward(lam, start, end)
        wavelength_range, flux_range = lamfluxrange(start, end, lam, cont_norm_flux)
        plt.close('all')
        fig = plt.figure()
        plt.plot(wavelength_range, flux_range, ds='steps')
        plt.show()
    elif(cmd == 'e'):
        lam_start, lam_end = get_limits()
        eqw, err = eq_width(lam, cont_norm_flux, cont_norm_flux_err, lam_start, lam_end)
        print("The Equivalent width of the line is: " + str(eqw) + " Å +/- " + str(err) + " Å")
    elif(cmd == 'z'):
        lam_start, lam_end = get_limits()
        z = np.float(input("Enter the redshift of the object: "))
        eqw, err = zeq_width(z, lam, cont_norm_flux, cont_norm_flux_err, lam_start, lam_end)
        print("The Rest-frame Equivalent width of the line is: " + str(eqw) + " Å +/- " + str(err) + " Å")
    else:
        print("Invalid character entered!")
    cmd = input("Enter a command (d for forward, a for backward,  e for equivalent width, h for halt, z for redshift): ")