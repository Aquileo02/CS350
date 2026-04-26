import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 18
GPIO.setup(ledPin, GPIO.OUT)

# Set up PWM on GPIO 18 at 100 Hz
pwm18 = GPIO.PWM(ledPin, 100)

# Start PWM with 50% duty cycle
pwm18.start(50)

try:
    while True:
        # Fade in
        for dutyCycle in range(0, 101, 5):
            pwm18.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

        # Fade out
        for dutyCycle in range(100, -1, -5):
            pwm18.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

pwm18.stop()
GPIO.cleanup()
