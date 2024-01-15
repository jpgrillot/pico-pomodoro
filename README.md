# pico-pomodoro
Pomodoro timer using the Raspberry Pico and Pimoroni Unicorn hat.

The Pomodoro technique is a time management practice where tasks are broken into chunks of time of focus and rest. The standard threshold is 25 minutes of focus and 5 minutes of rest. Some practice pomodoros using t-shirt sizing (small, medium, or large).

This timer is based on the [Picopomodoro timer](https://github.com/nikrawlinson/picopomodoro) from Nik Rawlinson with some tweaks.

The timer has three buttons to start:
  * The A button starts the "Large" size timer (45 minutes of focus and 15 minutes of rest). The LEDs illuminate Red with slight blue tint for this phase.
  * The X button starts the "Regular" size timer (25 minutes of focus and 5 mins of rest). The LEDs illuminate in Red for this phase.
  * The Y button starts the "Small" size timer (10 minutes of focus and 5 mins of rest). The LEDs illuminate in Orange for this phase.
  * The Rest phase is illuminated with Green LEDs.
  * The B button stops the timer. 
  * When the rest cycle completes, the timer will restart to the Large size if it was running the large size, or default to the Regular size.

## Install Instructions
### What you need
  * Raspberry Pi Pico with header pins installed (wireless version is not necessary)
  * Pimoroni Pico Unicorn hat
  * A desktop computer with Thonny IDE

### Setup and Install
  1. Install the Pimoroni Pico Firmware (version 1.21.0 latest tested) [firmware](https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md)
  1. Connect the Pico to your machine and open Thonny
  1. Copy the contents of main.py to your Thonny IDE and save the file on the pico as main.py
  1. Run the file and confirm it works.
  1. Unplug and connect to a powersource to run indepenedently.

## High Level Design
There are 112 LEDs, the multiplier is the number of seconds the LED must stay illuminated (in 10ths of a second) divided by the 112 LEDs. 5 minutes is 300 seconds, divided by 112 LEDs, equals 27 as the multiplier.

When you press the X or Y button the pomocycle method is called and passes through the value for the Phase variable. So, when you press X, the phase is set to "regular". There is an if statement that sets the multiplier, and LED color based on the phase. 

When the counter for Regular or Small completes, it cycles the Rest phase timer. When Rest completes, it cycles to the Regular phase.

## Ideas you might want to try
  * Change the LED colors (rgb)
  * Create a loop where after completing 4 pomodoros, the final Rest cycle is 15 minutes instead of 5
  * Flash the LEDs when a cycle has completed
