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
# Disable any in use warnings
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
RED=11
AMBER=16
GREEN=7

# Set Pin 11,16 and 7 on the GPIO header to act as an output
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(AMBER,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

# This loop runs forever and flashes the LED
while True:
	# Turn on the red LED
	GPIO.output(RED,GPIO.HIGH)
	print "Red"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the red LED
	GPIO.output(RED,GPIO.LOW)
	# Turn on the green LED
	GPIO.output(GREEN,GPIO.HIGH)
	print "Green"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the green LED
	GPIO.output(GREEN,GPIO.LOW)
	# Turn on the amber LED
	GPIO.output(AMBER,GPIO.HIGH)
	# Wait for 2 seconds
	time.sleep(2)
	GPIO.output(AMBER,GPIO.LOW)
