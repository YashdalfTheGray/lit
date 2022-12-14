import time
import neopixel
import board
import displayio
import terminalio
import ssl
import wifi
import socketpool

from adafruit_display_text import label
import adafruit_displayio_sh1107
import adafruit_ina219
import adafruit_requests


def wifi_connect():
    try:
        from secrets import secrets  # type: ignore
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise

    wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("My IP address is", wifi.radio.ipv4_address)
    return secrets["ssid"]


def init_display(main_group):
    color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=0, y=0)
    main_group.append(bg_sprite)


displayio.release_displays()
# oled_reset = board.D9

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
ina219_sensor = adafruit_ina219.INA219(i2c, addr=0x40)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
JSON_STARS_URL = "https://api.github.com/repos/adafruit/circuitpython"

connected_ssid = wifi_connect()
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)
splash = displayio.Group()
display.show(splash)
init_display(splash)

voltage_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=8)
splash.append(voltage_label)
current_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=20)
splash.append(current_label)
power_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=32)
splash.append(power_label)
ssid_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=44)
splash.append(ssid_label)
ipv4_label = label.Label(
    terminalio.FONT, text=" "*20, scale=1, color=0xFFFFFF, x=4, y=56)
splash.append(ipv4_label)

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

print("Fetching and parsing json from", JSON_STARS_URL)
response = requests.get(JSON_STARS_URL)
print("-" * 40)
print("CircuitPython GitHub Stars", response.json()["stargazers_count"])
print("-" * 40)

while True:
    current_color = predefined_colors[index]
    pixels.fill(current_color)
    voltage_label.text = "Voltage: {}V".format(ina219_sensor.bus_voltage)
    current_label.text = "Current: {}mA".format(ina219_sensor.current)
    power_label.text = "Power: {}W".format(ina219_sensor.power)
    if connected_ssid:
        ssid_label.text = "SSID: {}".format(connected_ssid)
        ipv4_label.text = "IP: {}".format(wifi.radio.ipv4_address)

    time.sleep(1)
    index = (index + 1) % predefined_colors_length
