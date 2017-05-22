#!/usr/bin/python3

'''
Detects movement from the PIR Motion Sensor
'''

# Builtin Python Libraries
import os
from time import sleep

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'PIR Motion Selsor Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}PIR Status: {s}'
STATUS = ''

# Create some dynamic controls
WAIT_TIME = 2.5 # Number in seconds
PREV_STATE = 0

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = [15, 18]
GPIO.setup(GPIO_LIST, GPIO.OUT)
GPIO_PIR = 7
GPIO.setup(GPIO_PIR, GPIO.IN)

def update_display():
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, s=STATUS))

try:
    while True:
        # Loop until PIR output is 0
        while GPIO.input(GPIO_PIR) == 1:
            STATUS = 'Trying to detect Motion'

        # Loop until users quits with CTRL-C
        while True:
            # Read PIR state
            if GPIO.input(GPIO_PIR) == 1  and PREV_STATE == 0:
                # Set Status
                STATUS = 'Motion detected!'

                # Update outputs
                GPIO.output(GPIO_LIST, GPIO.HIGH)

                # Set PREV_STATE
                PREV_STATE = 1

            elif GPIO.input(GPIO_PIR) == 0  and PREV_STATE == 1:
                # Set status
                STATUS = 'Waiting for movement'

                # Update outputs
                GPIO.output(GPIO_LIST, GPIO.LOW)

                # Set PREV_STATE
                PREV_STATE = 0

            update_display()
            sleep(0.2)

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
finally:
    GPIO.cleanup()
