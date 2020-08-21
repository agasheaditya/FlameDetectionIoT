import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buzzer = 23

GPIO.setup(buzzer, GPIO.OUT)
try:
 while True:
  GPIO.output(buzzer, GPIO.HIGH)
  print('BEEEP')
  sleep(0.5)
  GPIO.output(buzzer, GPIO.LOW)
  print('NO BEEP')
  sleep(0.5)

finally:
 GPIO.cleanup(buzzer)
 GPIO.setwarnings(False)
