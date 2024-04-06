import RPi.GPIO as GPIO
from time import sleep
import time

ssr_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

while True:
  GPIO.output(ssr_pin, True)
  time.sleep(100.0)
  GPIO.output(ssr_pin, False)
  time.sleep(300.0)
