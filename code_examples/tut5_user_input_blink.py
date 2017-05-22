#!/usr/bin/python3

'''
Makes an LED blink on and off a set number of times
depending on user input
'''

# Builtin Python Libraries
import os
from time import sleep

# Installed Libraries
import RPi.GPIO as GPIO

HEADER = 'User Input Blink Test (Ctrl+C to Quit)\n\n'
DISPLAY = '{h}LED Status: {s}\nLoop Count: {lc}/{tl}'

# Create some dynamic controls
WAIT_TIME = 1 # Number in seconds
LOOP_COUNT = 0

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

def led_blink(led, count):
    '''makes the selected LED blink depending on users input'''

    for loops in range(0, count):
        GPIO.output(GPIO_LIST[led], GPIO.HIGH)
        update_display('ON', loops)
        GPIO.output(GPIO_LIST[led], GPIO.LOW)
        update_display('OFF', loops)


try:
    while True:
        try:
            # Clear the console
            os.system('clear')
            print('{}Which LED would you like to blink\n 1: Red\n 2: Blue\n 3: Quit'.format(HEADER))

            # Get the user to make a selection
            LED_CHOICE = int(input('\nPlease make your choice: '))

            # Clear the console
            os.system('clear')

            # Check the user's choice to see if valid
            if LED_CHOICE == 1 or LED_CHOICE == 2:
                if LED_CHOICE == 1:
                    print('{}You Selected the RED LED\n'.format(HEADER))
                elif LED_CHOICE == 2:
                    print('{}You Selected the BLUE LED\n'.format(HEADER))

                # get the user to enter how meny times to make the LED to blink
                LOOP_COUNT = int(input('How many times should it blink?: '))

                #Make the selected LED blink the select amount of times
                led_blink(LED_CHOICE-1, LOOP_COUNT)
            elif LED_CHOICE == 3:
                break

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
