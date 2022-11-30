"""This example uses the NeoPixels. It shows three different LED animation types in many colors."""
import time
import board
import neopixel
import digitalio

pixels = neopixel.NeoPixel(
    board.NEOPIXEL, 10, brightness=0.3, auto_write=False)

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN


def color_wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j
            pixels[i] = color_wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

show_leds = False

while True:
    if button_a.value:
        show_leds = True

    if button_b.value:
        show_leds = False

    if show_leds:
        pixels.fill(RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(1)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(1)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(1)

        # Increase the number to slow down the color chase
        color_chase(RED, 0.1)
        color_chase(YELLOW, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(CYAN, 0.1)
        color_chase(BLUE, 0.1)
        color_chase(PURPLE, 0.1)

        rainbow_cycle(0)  # Increase the number to slow down the rainbow
