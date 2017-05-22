#!/usr/bin/python3

'''
Turns 2 LED's on and off
'''

# Builtin Python Libraries
import os

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'LED ON/OFF Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}LED Status: {s}'

# Create some dynamic controls
WAIT_TIME = 3 # Number in seconds

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = [15, 18] # 15=Red LED, 18=Blue LED
GPIO.setup(GPIO_LIST, GPIO.OUT)

def update_display(status):
    ''' Updates the text displayed in the console '''

    # Clear the console
    os.system('clear')

    # Print the formatted text to the console
    print(DISPLAY.format(h=HEADER, s=status))

# Switch the LEDs on
GPIO.output(GPIO_LIST, GPIO.HIGH)

# Update the console text
update_display('ON')
