# coding:utf-8
import RPi.GPIO as GPIO
import time
import sys

Led_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_pin, GPIO.OUT)

Led = GPIO.PWM(Led_pin, 50)

Led.start(0)
bright = 1

while True:
    try:
        for _ in range(1):
            Led.ChangeDutyCycle(bright)
            print(bright)
            time.sleep(2)
            # 点滅させる
            # Led.ChangeDutyCycle(0)
            # time.sleep(0.5)
        bright *= 2
        if bright > 32:
            bright = 1
            
    except KeyboardInterrupt:
        Led.stop()
        GPIO.cleanup()
        sys.exit()