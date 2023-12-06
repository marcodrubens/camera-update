import RPi.GPIO as GPIO
PIN = 18 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

while True: # Run forever
    if GPIO.input(PIN) == GPIO.HIGH:
        print("Button was pushed!")