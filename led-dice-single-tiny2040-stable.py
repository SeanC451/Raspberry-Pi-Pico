# LED Single Dice on Tiny2040

# Circuit:
#    Six LEDs +ve connected to six 220Ω Resistors to Pins 1-6 -ve to GND.
#    Touch switch connected to Pin 26 (Analog A0) and PWR rail.
#    Tiny2040 5v (0) and Ground (1) to PWR and GND rails.


# Imports

import machine, utime, random

# Declarations

timer = .05                              # Delay timer to flash LEDs
hold = 2                                 # Delay timer after roll. Change to adjust.

LED_pips = [1,2,3,4,5,6]

for pin in LED_pips:
    machine.Pin(pin, machine.Pin.OUT)

button = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Functions

def zipPips():                             # Function to turn on remaning LEDs and then all off.
    for x in range(0,6):
        LED = machine.Pin(LED_pips[x])
        if LED.value() != 1:
            LED.toggle()
            utime.sleep(timer)
    utime.sleep(timer)
    for x in range(5,-1,-1):
        LED = machine.Pin(LED_pips[x])
        LED.toggle()
        utime.sleep(timer)

def flashPips():                           # Function to turn LEDs on and off.
    for x in range(0,6):
        LED = machine.Pin(LED_pips[x])
        LED.toggle()
        utime.sleep(timer)
    for x in range(5,-1,-1):
        LED = machine.Pin(LED_pips[x])
        LED.toggle()
        utime.sleep(timer)

def flashRoll():                           # Function to display random die roll.
    if (ran >= 1):
        LED = machine.Pin(LED_pips[0])
        LED.toggle()
    if (ran >= 2):
        LED = machine.Pin(LED_pips[1])
        LED.toggle()
    if (ran >= 3):
        LED = machine.Pin(LED_pips[2])
        LED.toggle()
    if (ran >= 4):
        LED = machine.Pin(LED_pips[3])
        LED.toggle()
    if (ran >= 5):
        LED = machine.Pin(LED_pips[4])
        LED.toggle()
    if (ran >= 6):
        LED = machine.Pin(LED_pips[5])
        LED.toggle()
    utime.sleep(hold)
    zipPips()

    
# Loop

while True:
    ran = random.randint(1, 6)
    if button.value() == 1:
        print("Roll =",ran)                    # Debug/Comment out to stop Serial Print.
        flashPips()
        flashRoll()
