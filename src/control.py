import RPi.GPIO as GPIO
import time
#import logging

#logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,filename='/App/gpio.log')

# Set GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BCM) 

# GPIO pins list based on GPIO.BOARD
# gpioList1 = [17,18]
# gpioList2 = [14,15]

# Set mode for each gpio pin
GPIO.setup(17, GPIO.OUT, initial= GPIO.HIGH)
GPIO.setup(18, GPIO.OUT, initial= GPIO.LOW)

#GPIO.setup(gpioList2, GPIO.IN)

def set_status(pin,status):
    GPIO.output(pin, status)

