#!/usr/bin/python3

'''
Sounds a buzzer and flashes LEDs for Morse Code
'''

# Builtin Python Libraries
import os
from time import sleep

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'Morse Code Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}Loop Count: {lc}/{tl}'

# Create some dynamic controls
SHORT_WAIT = 0.1 # Number in seconds
LONG_WAIT = 0.2
LOOP_WAIT = 1
LOOP_COUNT = 0

# Set the pin numbering system
# Modes Available: GPIO.BCM, GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set the GPIO Warnings
# True = enable, False = Disable
GPIO.setwarnings(False)

# Setup the pins to use
GPIO_LIST = [15, 18, 25] # 15=Red LED, 18=Blue LED, 25=Buzzer
GPIO.setup(GPIO_LIST, GPIO.OUT)

def update_display(loop_count):
    ''' Updates the text displayed in the console '''
    # Clear the console
    os.system('clear')

    # Print the formatted text
    print(DISPLAY.format(h=HEADER, lc=loop_count + 1, tl=LOOP_COUNT))

def set_outputs(wait):
    ''' Sets the outputs on and off with a specified wait time '''
    GPIO.output(GPIO_LIST, GPIO.HIGH)
    sleep(wait)
    GPIO.output(GPIO_LIST, GPIO.LOW)
    sleep(wait)

def morsecode():
    ''' Morse Code loops structure '''
    # 3 short bursts on buzzer and LEDs
    for x in range(0, 3):
        set_outputs(SHORT_WAIT)
    sleep(SHORT_WAIT)
    # 3 long bursts on buzzer and LEDs
    for x in range(0, 3):
        set_outputs(LONG_WAIT)

    # 3 short bursts on buzzer and LEDs1
    for x in range(0, 3):
        set_outputs(SHORT_WAIT)

    # Waits a specified time before restarting loop
    sleep(LOOP_WAIT)

try:
    while True:
        try:
            os.system('clear')
            print(HEADER)

            # Gets the user input
            LOOP_COUNT = int(input('How many times would you like SOS to loop?: '))

            # Loops the morse code for the specified amount of times
            for count in range(0, LOOP_COUNT):
                update_display(count)
                morsecode()
        except (ValueError, SyntaxError):
            # If the input is not a number then let the user know and restart
            print('Invalid input, must be a number, Please try again')
            sleep(3)
            os.system('clear')

# when CTRL+C is pressed, terminate the program and cleanup
except KeyboardInterrupt:
    print('\nTerminating Program')
finally:
    GPIO.cleanup()
