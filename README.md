# Gators in Motion

Interactive kinetic sculpture system using a Raspberry Pi 5, DRV8825 stepper motor driver, NEMA 17 stepper motor, and magnetic reed switch sensor. The installation activates motion when a door opens and runs for a programmable amount of time.

---

# Components

## Main Electronics
- Raspberry Pi 5
- MicroSD Card
- Raspberry Pi Power Supply
- NEMA 17 Stepper Motor (42-40)
- DRV8825 Stepper Motor Driver
- 12V 5A Power Supply
- Magnetic Reed Switch Sensor
- Breadboard
- Jumper Wires
- 22 AWG Wire
- Capacitor (100uF–470uF, 25V)
- Inline Fuse Holder
- 5A Slow-Blow Fuse
- DC Rocker Switch
- Screw Terminal Connectors

## Assembly Materials
- Heat Shrink Tubing
- Zip Ties
- Adhesive Cable Clips

---

# System Logic

1. Door opens
2. Magnet separates from reed switch
3. Raspberry Pi detects trigger
4. DRV8825 receives STEP and DIR signals
5. Stepper motor rotates sculpture
6. System runs for programmed duration
7. Cooldown timer prevents immediate retriggering

---

# Raspberry Pi GPIO Pins

| Function | GPIO | Physical Pin |
|---|---|---|
| STEP | GPIO23 | Pin 16 |
| DIR | GPIO24 | Pin 18 |
| Sensor Input | GPIO17 | Pin 11 |
| Logic GND | GND | Pin 14 |
| Sensor GND | GND | Pin 6 |
| 3.3V | 3.3V | Pin 1 |

---

# DRV8825 Wiring

## Logic Side

### STEP
Raspberry Pi GPIO23 (Pin 16)  
→ DRV8825 STEP

### DIR
Raspberry Pi GPIO24 (Pin 18)  
→ DRV8825 DIR

### Logic Ground
Raspberry Pi GND (Pin 14)  
→ DRV8825 Logic GND

### RESET + SLEEP
Connect RESET and SLEEP together.

Then connect:  
→ Raspberry Pi Pin 1 (3.3V)

### ENABLE
Connect ENABLE  
→ Logic GND

---

# Motor Power Wiring

## Positive Power Path

12V Power Supply (+)  
→ Inline Fuse Holder  
→ Rocker Switch RED wire  
→ Other RED wire from rocker switch  
→ DRV8825 VMOT

## Negative Power Path

12V Power Supply (-)  
→ DRV8825 GND next to VMOT

---

# Rocker Switch Notes

The rocker switch has:
- 2 red wires
- 2 black wires

Use ONLY the red wires.

The black wires are typically for the internal LED and are not required.

---

# Capacitor Installation

Install capacitor across:

VMOT ↔ GND

on the DRV8825 motor power side.

---

# Stepper Motor Wiring

| DRV8825 Pin | Motor Wire |
|---|---|
| A1 | Black |
| A2 | Green |
| B1 | Red |
| B2 | Blue |

If the motor locks but does not rotate:
- swap coil pairs
- verify motor wiring with multimeter continuity mode

---

# Reed Switch Wiring

| Reed Switch Terminal | Connection |
|---|---|
| NO | Raspberry Pi GPIO17 (Pin 11) |
| COM | Raspberry Pi GND (Pin 6) |

---

# Reed Switch Installation

The reed switch has:
1. Sensor body
2. Magnet piece

Mount:
- sensor body on door frame
- magnet on moving door

When the door opens, the magnet separates from the sensor and triggers the system.

---

# Raspberry Pi Setup

## 1. Install Raspberry Pi OS

Use Raspberry Pi Imager to install:
- Raspberry Pi OS (64-bit)

onto the MicroSD card.

Insert SD card into Raspberry Pi.

---

## 2. Connect Peripherals

Connect:
- monitor using Micro HDMI
- USB keyboard
- USB mouse
- Raspberry Pi USB-C power supply

Power on Raspberry Pi.

---

# VS Code Setup

```bash
sudo apt update
sudo apt install code -y
```

Install GPIO library:

```bash
pip install RPi.GPIO
```

---

# Running the Program

Save Python file as:

```bash
main.py
```

Run:

```bash
python3 main.py
```
---

# DRV8825 Cooling

Install heatsink directly on DRV8825 chip.

Recommended for long runtime operation.
