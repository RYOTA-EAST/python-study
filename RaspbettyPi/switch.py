import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(25, GPIO.OUT)
for i in range(50): 
    print(i, GPIO.input(21))
    if GPIO.input(21):
        GPIO.output(25, GPIO.HIGH)
        sleep(1)
    else:
        GPIO.output(25, GPIO.LOW)
        sleep(1)
GPIO.cleanup()