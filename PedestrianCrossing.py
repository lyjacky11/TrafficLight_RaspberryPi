# First we need to import the libraries that
# we need
# Import the time library so that we can make
# the program pause for a fixed amount of time
import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins

# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
 # Set up the pin numbers we are using for each LED
RED=11
AMBER=16
GREEN=7

# Define the pin for the switch
SWITCH=22

# Set Pin 11, 16 and 7 on the GPIO header to act as an output
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(AMBER,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

# Set up pin 22 (SWITCH) to act as an input
GPIO.setup(SWITCH,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# This loop runs forever and runs the traffic lights sequence
while True:
    # Turn on the green LED
    GPIO.output(GREEN,GPIO.HIGH)
    print "Green"
    ButtonPressed = False

    # Wait until a pedestrian presses the switch
    print "Press button"
    while not ButtonPressed:
        # Wait for 2 seconds
        time.sleep(1)
        ButtonPressed = GPIO.input(SWITCH)

    print "Button pressed"
    # Turn off the green LED
    GPIO.output(GREEN,GPIO.LOW)
    # Turn on the amber LED
    GPIO.output(AMBER,GPIO.HIGH)
    print "Amber"
    # Wait for 2 seconds
    time.sleep(2)
    # Turn off the amber LED
    GPIO.output(AMBER,GPIO.LOW)
    # Turn on the red LED
    GPIO.output(RED,GPIO.HIGH)
    print "Red"
    # Wait for 4 seconds
    time.sleep(4)
    # Turn off the red LED
    GPIO.output(RED,GPIO.LOW)

    # Now flash the amber light
    count = 5
    while count > 0:
        # Turn on the amber LED
	print "Flash amber"
        GPIO.output(AMBER,GPIO.HIGH)
        time.sleep(1)
        # Turn off the amber LED
        GPIO.output(AMBER,GPIO.LOW)
        time.sleep(1)
	count = count - 1

# End of code	
