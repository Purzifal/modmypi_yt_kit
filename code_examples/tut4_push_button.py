#!/usr/bin/python3

'''
Turns an LED on and off depending on the state of
a push button
'''

# Builtin Python Libraries
import os
from time import sleep

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'Push Button Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}Push Button Status: {s}'

# Create some dynamic controls
WAIT_TIME = 2 # Number in seconds

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = [15, 18] # 15=Red LED, 18=Blue LED
GPIO_BUTTON = 23
GPIO.setup(GPIO_LIST, GPIO.OUT)
GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def update_display(status):
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, s=status))

try:
    # Update the consle text
    update_display('Waiting for button to be pressed')

    # Loop until Ctrl+C is pressed
    while True:

        # Check to see if push button has been pressed
        if not GPIO.input(GPIO_BUTTON): # 0 = button is pressed

            # Update the console text
            update_display('Pressed\nResetting in {} seconds'.format(WAIT_TIME))

            # Turn the LEDs on
            GPIO.output(GPIO_LIST, GPIO.HIGH)

            # Wait a specified amount of time
            sleep(WAIT_TIME)

            # Turn the LEDs off
            GPIO.output(GPIO_LIST, GPIO.LOW)

            # Update the console text
            update_display('Waiting for button to be pressed')
        else:
            # If the button is not pressed wait 0.05 secs
            # This is just to reduce CPU Load
            sleep(0.05)

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
finally:
    GPIO.cleanup()
