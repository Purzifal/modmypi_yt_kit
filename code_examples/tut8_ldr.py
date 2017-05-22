#!/usr/bin/python3

'''
Reads the light level from the Light Dependant Resistor
'''

# Builtin Python Libraries
import os
from time import sleep
from datetime import datetime

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'LDR Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}Date & Time : {d}\nLDR Reading : {ldr}'

# Create some dynamic controls
WAIT_TIME = 1 # Number in seconds

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = 3 # 15=Red LED, 18=Blue LED, 25=Buzzer
GPIO.setup(GPIO_LIST, GPIO.OUT)

def update_display(date, ldr):
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, d=date, ldr=ldr))

def get_reading():
    ''' Measures the light level from the LDR '''
    reading = 0
    # set the GPIO to an output
    GPIO.setup(GPIO_LIST, GPIO.OUT)
    GPIO.output(GPIO_LIST, GPIO.LOW)
    sleep(.1)

    # set GPIO to an input
    GPIO.setup(GPIO_LIST, GPIO.IN)

    # measure the reading
    while GPIO.input(GPIO_LIST) == GPIO.LOW:
        reading += 1

    # return the reading
    return str(reading)

try:
    while True:
         # Get the current datetime and format it
        DATE_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Get the reading from the LDR and format it to a string
        LDR_READING = get_reading()

        # format the string to a readable layout
        update_display(DATE_TIME, LDR_READING)

        # Open a file and write a formatted string to the file
        FILE = open("Data/ldr_data.txt", "w")
        FILE.write(DISPLAY.format(h='', d=DATE_TIME, ldr=LDR_READING))
        FILE.close()

        # Wait specified time
        sleep(WAIT_TIME)

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
finally:
    GPIO.cleanup()
