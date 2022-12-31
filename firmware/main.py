import time
import neopixel
import board
import displayio
import terminalio

from adafruit_display_text import label
import adafruit_displayio_sh1107


def clamp(x):
    return max(0, min(x, 255))


def tuple_to_hashcode(color_tuple):
    return "#{0:02x}{1:02x}{2:02x}".format(
        clamp(color_tuple[0]),
        clamp(color_tuple[1]),
        clamp(color_tuple[2])
    )


def init_display(main_group):
    color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    main_group.append(bg_sprite)


displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

splash = displayio.Group()
display.show(splash)
init_display(splash)
color_hash_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=8)
splash.append(color_hash_label)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

INTENSITY = 0.05
color_value = round(INTENSITY * 255)
predefined_colors = [
    (color_value, 0, 0),
    (color_value, color_value, 0),
    (0, color_value, 0),
    (0, color_value, color_value),
    (0, 0, color_value),
    (color_value, 0, color_value)
]
predefined_colors_length = len(predefined_colors)
index = 0

while True:
    current_color = predefined_colors[index]
    pixels.fill(current_color)
    color_hash_label.text = f"Color: {tuple_to_hashcode(current_color)}"
    time.sleep(1)
    index = (index + 1) % predefined_colors_length
