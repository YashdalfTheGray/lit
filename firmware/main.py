import time
import neopixel
import board
import displayio
import terminalio

# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000

bg_sprite = displayio.TileGrid(
    color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw some label text
text1 = "0123456789ABCDEF123456789AB"  # overly long to see where it clips
text_area = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area)
text2 = "SH1107"
text_area2 = label.Label(
    terminalio.FONT, text=text2, scale=2, color=0xFFFFFF, x=9, y=44
)
splash.append(text_area2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

INTENSITY = 0.05
color_value = round(INTENSITY * 255)

while True:
    pixels.fill((color_value, 0, 0))
    time.sleep(0.5)
    pixels.fill((color_value, color_value, 0))
    time.sleep(0.5)
    pixels.fill((0, color_value, 0))
    time.sleep(0.5)
    pixels.fill((0, color_value, color_value))
    time.sleep(0.5)
    pixels.fill((0, 0, color_value))
    time.sleep(0.5)
    pixels.fill((color_value, 0, color_value))
    time.sleep(0.5)
