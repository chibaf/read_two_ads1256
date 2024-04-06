import RPi.GPIO as GPIO
from time import sleep
import time

ssr_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

while True:
  GPIO.output(ssr_pin, True)
  print("SSR ON (200sec)\n")
  time.sleep(200.0)
  GPIO.output(ssr_pin, False)
  print("SSR OFF (200sec)\n")
  time.sleep(200.0)
