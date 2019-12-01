import RPi.GPIO as GPIO
import time

servoPIN = 18
servoPIN2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p=GPIO.PWM(servoPIN, 50)
p2 = GPIO.PWM(servoPIN2, 50)
p.start(5)
p2.start(5)
#1-11
p.ChangeDutyCycle(11)
p2.ChangeDutyCycle(11)
time.sleep(1.5)

p.stop()
