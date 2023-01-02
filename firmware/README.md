# Firmware

## Version

```json
{
  "circuitpython.board.version": "8.0.0-beta.5"
}
```

Firmware - https://circuitpython.org/board/adafruit_feather_esp32s3_4mbflash_2mbpsram/
Docs - https://docs.circuitpython.org/en/latest/docs/index.html
OfficialBundle - https://github.com/adafruit/Adafruit_CircuitPython_Bundle
CommunityBundle - https://github.com/adafruit/CircuitPython_Community_Bundle

## Copying libraries out of the archive

```sh
./firmware/copy-lib -d -a firmware/adafruit-circuitpython-bundle-8.x-mpy-20221216.zip -l ./firmware/libraries.json
```

## Notes

### Display

- While printing text on the screen, `scale=1` (which is the default) represents characters that are 8 pixels tall. And this scales linearly, so `scale=2` is 16 pixels.
- For printing, `x=0, y=4` actually represents the area of the screen where you can actually start seeing the text. `x=0, y=0` will cut out some of the text. The actual bounds of the screen are `[0,127]` in the x-axis and `[4, 68]` in the y-axis.
- To change text on the screen, we just need to update the text on the label created from `label.Label` using `label_instance.text = "the new text"`. The `label` import is available from the `adafruit_display_text` library.

### INA219

- The `shunt_voltage` is the voltage differential between the + and - terminals on the board
- The `bus_voltage` is the voltage differential between the - terminal and ground
- _Technically_, the `current` and the `bus_voltage` numbers should multipled together should match the `power` number but that only happens when there is an actual load on the circuit.
- Since we're using an external 5V 5A power supply, we expect the `bus_voltage` to read close to 5V all the time once it is hooked up.
- Learning that we might need the INA260 instead of the INA219 to do the current/voltage measurement since the INA219 featherwing comes with a 0.1 ohm current sense resistor which makes the measurable current range +/-3.2A.
- With the loss of some precision, a current range of +/-32A can be achieved but the 0.1 ohm current sense resistor needs to be replaced with a 0.01 ohm resistor.
- The INA260 comes with a 0.02 ohm current sense resistor which can measure up to 15A of current on the high side.

### Wifi

- The SSID and password are stored in a file called `secrets.py` in the root of the `CIRCUITPY` drive.
- There doesn't seem to be a way to create a server that listens for requests against it but you can make outbound requests using the `adafruit_requests` library
- The `wifi.radio.ipv4_address` property can be used to get the IP address of the controller on the network
- expect upto 10 seconds of latency when powering up with wifi, it takes some time to connect and establish all the proper sockets for outbound requests

## References

- https://github.com/adafruit/PyCon2019
- https://learn.adafruit.com/adafruit-circuit-playground-express
- https://learn.adafruit.com/sipping-power-with-neopixels
- https://learn.adafruit.com/adafruit-neopixel-uberguide/powering-neopixels
- https://www.adafruit.com/product/4650
- https://www.adafruit.com/product/3650
- https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout
- https://learn.adafruit.com/adafruit-128x64-oled-featherwing
- https://learn.digilentinc.com/Documents/390
