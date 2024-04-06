import RPi.GPIO as GPIO
from time import sleep
import time

ssr_pin = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

while True:
#  pwm_totaltime=10.0
#  pwm_width=0.5
#  on_time=pwm_totaltime*pwm_width
#  off_time=pwm_totaltime*(1-pwm_width)
  GPIO.output(ssr_pin, True)
  time.sleep(8.0)
  GPIO.output(ssr_pin, False)
  time.sleep(2.0)