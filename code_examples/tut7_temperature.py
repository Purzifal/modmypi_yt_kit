#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Displays the temperature in celsius and fahrenheit
'''

# Builtin Python Libraries
import os
from glob import glob

HEADER = 'Temperature Sensor Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}Temp (°C): {c}\nTemp (°F): {f}'

# Program Variables
BASE_LOC = '/sys/bus/w1/devices/'
DEVICE_LOC = '{}/w1_slave'.format(glob(BASE_LOC + '28*')[0])

def update_display(celsius, fahrenheit):
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, c=celsius, f=fahrenheit))

def get_temp():
    '''reads a specific file from the system and extracts the temperature data'''
    read_file = open(DEVICE_LOC, 'r')
    tmp_txt = read_file.readlines()
    read_file.close()
    return round(float(tmp_txt[1].split(' ')[9][2:-1])/1000, 1)

try:
    while True:
        TEMPERATURE = [get_temp(), round((get_temp() * 1.8) + 32, 1)]
        update_display(TEMPERATURE[0], TEMPERATURE[1])

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
