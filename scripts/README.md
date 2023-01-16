# Scripts

## General info

These scripts are mostly here to help out with CircuitPython development. Each script supports passing in `--help` to give you more information about what it does and how to customize it.

## Links

OfficialBundle - https://github.com/adafruit/Adafruit_CircuitPython_Bundle
CommunityBundle - https://github.com/adafruit/CircuitPython_Community_Bundle

## Download the latest archives from Github

This assumes that you're in the project root. You also need to run a `pip install -r requirements.txt` before you can use this script.

```sh
./scripts/fetch-latest-libraries -o firmware -t <your_github_api_token> -c 8.x
```

## Copying libraries out of downloaded archives

This assumes that you're in the project root.

```sh
./scripts/copy-lib -d -a firmware/adafruit-circuitpython-bundle-8.x-mpy-20221216.zip -l ./firmware/libraries.json
```

## Update the `requirements.txt file`

This assumes you're in the scripts folder and you have `pipreqs` installed. If not, install using `pip install pipreqs`.

```
mv fetch-latest-libraries fetch-latest-libraries.py && mv copy-lib copy-lib.py && pipreqs --debug --force --mode compat . && mv copy-lib.py copy-lib && mv fetch-latest-libraries.py fetch-latest-libraries
```
