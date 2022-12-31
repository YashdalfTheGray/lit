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

## References

- https://github.com/adafruit/PyCon2019
- https://learn.adafruit.com/adafruit-circuit-playground-express
- https://learn.adafruit.com/sipping-power-with-neopixels
- https://learn.adafruit.com/adafruit-neopixel-uberguide/powering-neopixels
- https://www.adafruit.com/product/4650
- https://www.adafruit.com/product/3650
- https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout
- https://learn.adafruit.com/adafruit-128x64-oled-featherwing
