#!/usr/bin/python3

'''
Makes both LEDs blink on and off a set number of times
'''

# Builtin Python Libraries
import os
from time import sleep

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'LED Blink Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}LED Status: {s}\nLoop Count: {lc}/{tl}'

# Create some dynamic controls
WAIT_TIME = 1 # Number in seconds
LOOP_COUNT = 5

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = [15, 18] # 15=Red LED, 18=Blue LED
GPIO.setup(GPIO_LIST, GPIO.OUT)

def update_display(status, loop_count):
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, s=status, lc=loop_count + 1, tl=LOOP_COUNT))

    # Wait the specified amount of time
    sleep(WAIT_TIME)

try:
    for loops in range(0, LOOP_COUNT):

        # Switch the LEDs on
        GPIO.output(GPIO_LIST, GPIO.HIGH)

        # Update the console text
        update_display('ON', loops)

        # Switch the LEDs off
        GPIO.output(GPIO_LIST, GPIO.LOW)

        # Update the console text
        update_display('OFF', loops)

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
finally:
    GPIO.cleanup()
