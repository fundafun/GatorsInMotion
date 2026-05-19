
import RPi.GPIO as GPIO
import time
from datetime import datetime

RUN_TIME = 15          # how long motor runs after trigger (seconds)
COOLDOWN = 330         # lockout time after trigger (5 min = 300 sec)

START_HOUR = 7         # system active starting at 7 AM
END_HOUR = 17          # system stops at 5 PM (17 = 5 PM)

# Raspberry Pi GPIO pins
DOOR_SENSOR = 17       # Reed switch → GPIO17 → Physical Pin 11
STEP_PIN = 23          # DRV8825 STEP → GPIO23 → Physical Pin 16
DIR_PIN = 24           # DRV8825 DIR → GPIO24 → Physical Pin 18

GPIO.setmode(GPIO.BCM)

# Reed switch input with pull-up resistor
GPIO.setup(DOOR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Stepper motor driver pins
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Track last trigger time for cooldown
last_trigger_time = 0

print("System starting...")

# CHECK IF SYSTEM SHOULD RUN
# Mon–Fri only, 7 AM–5 PM

def system_active():
    now = datetime.now()

    # Monday = 0, Sunday = 6
    if now.weekday() >= 5:
        return False

    # active during selected hours
    if now.hour < START_HOUR or now.hour >= END_HOUR:
        return False

    return True

# =====================================
# RUN STEPPER MOTOR
# =====================================

def run_motor():
    print("Motor running...")

    # Set motor direction
    GPIO.output(DIR_PIN, GPIO.HIGH)

    end_time = time.time() + RUN_TIME

    while time.time() < end_time:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)

        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)

    print("Motor stopped.")


# =====================================
# MAIN LOOP
# =====================================

try:
    while True:

        # Reed switch trigger check
        # With NO + COM setup:
        # door event usually reads LOW (0)
        if GPIO.input(DOOR_SENSOR) == 0:

            current_time = time.time()

            # Check allowed schedule
            if not system_active():
                print("Outside active hours (Mon–Fri, 7AM–5PM)")
                time.sleep(1)
                continue

            # Check cooldown
            if current_time - last_trigger_time < COOLDOWN:
                print("Cooldown active. Waiting...")
                time.sleep(1)
                continue

            # Valid trigger
            print("Door triggered!")

            last_trigger_time = current_time

            run_motor()

            # small delay so it doesn’t instantly re-read
            time.sleep(1)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("System stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")