import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
buzzer = 23  # setting pin GPIO 23 as a constant to the variable
GPIO.setup(buzzer, GPIO.OUT) # setting pin 23 as a o/p pin

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
