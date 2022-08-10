import math
import utime
import picounicorn

picounicorn.init()
# The pomocycle accepts the phase variable to be passed to it.
def pomocycle(phase):
    # Set up the LED grid size
    column = 15
    row = 6

    # Start counting down
    while not(picounicorn.is_pressed(picounicorn.BUTTON_B)):
        # Set multiplier based on phase passed as well as the RGB variables
        if phase == "regular":
            multiplier = 134
            r = 255
            g = 0
        elif phase == "small":
            multiplier = 54
            r = 255
            g = 127
        # Default to rest phase
        else:
            multiplier = 27
            r = 0
            g = 255

        # Illuminate every LED on the board
        for x in range(16):
            for y in range(7):
                picounicorn.set_pixel(x, y, r, g, 0)
        
        # Extinguish LEDs one by one
        while row > -1:
            while column > -1:
                for x in range(multiplier):
                    if not(picounicorn.is_pressed(picounicorn.BUTTON_B)):
                           utime.sleep(0.1)
                    else:
                        break
                picounicorn.set_pixel(column, row, 0, 0, 0)
                column -= 1
            column = 15
            row -= 1
        row = 6
        
        # No more LEDs? If in rest phase switch to regular, otherwise default to rest
        if phase == "rest":
            phase = "regular"
        else:
            phase = "rest"

    # Clear the display
    for x in range(16):
        for y in range(7):
            picounicorn.set_pixel(x, y, 0, 0, 0)

while True:
    # When you press the X button, the pomocycle method will be called with the "Regular" phase variable
    while picounicorn.is_pressed(picounicorn.BUTTON_X):
        pomocycle(phase="regular")
    # When you press the Y button, the pomocycle method will be called with the "Small" phase variable
    while picounicorn.is_pressed(picounicorn.BUTTON_Y):
        pomocycle(phase="small")
