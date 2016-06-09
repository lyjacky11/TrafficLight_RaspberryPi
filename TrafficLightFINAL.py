import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
RED=11
AMBER=16
GREEN=7

# Set Pin 11,16 and 7 on the GPIO header to act as an output
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(AMBER,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

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
	print "Amber"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the amber LED
	GPIO.output(AMBER,GPIO.LOW)

# ADVANCE GREEN:
	
        # Turn on the red LED
	GPIO.output(RED,GPIO.HIGH)
	print "Red"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the red LED
	GPIO.output(RED,GPIO.LOW)



# LOOP:
for x in xrange(1, 21):
	# Turn on the LED
	GPIO.output(GREEN,GPIO.HIGH)
	print "Advance Green"
	# Wait for a second
	time.sleep(0.1)
	# Turn off the LED
	GPIO.output(GREEN,GPIO.LOW)
	# Wait for a second
	time.sleep(0.1)
	break

	# Turn on the green LED
	GPIO.output(GREEN,GPIO.HIGH)
	print "Green"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the green LED
	GPIO.output(GREEN,GPIO.LOW)
        # Turn on the amber LED
	GPIO.output(AMBER,GPIO.HIGH)
	print "Amber"
	# Wait for 2 seconds
	time.sleep(2)
	# Turn off the amber LED
	GPIO.output(AMBER,GPIO.LOW)
