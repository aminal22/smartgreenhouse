import RPi.GPIO as GPIO

SOIL_SENSOR_PIN = 17  # GPIO pin for soil humidity sensor

def get_soil_humidity():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)
    soil_status = GPIO.input(SOIL_SENSOR_PIN)
    if soil_status == GPIO.HIGH:
        return "Dry"
    else:
        return "Wet"
