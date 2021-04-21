# Tuxedo Polaris and XMG Core keyboard backlight tray menu for Linux

## Install dependencies
`sudo apt install python3-pyqt5` 

## Usage example

To change the color or brightness, `keyboard_service.py` needs root permission. 
To use the tray without sudo, you can add a line to the end of sudoers:

```bash
sudo visudo
your_use_name ALL=(ALL) NOPASSWD: path/to/keyboard_service.py
```

keyboard_tray.py and keyboard_service.py needs to be executable:

```bash
sudo chmod +x keyboard_service.py
sudo chmod +x keyboard_tray.py
```

Now you can add keyboard_tray.py to your autostart or run it with:

`./keyboard_tray.py`

All files need to be in the same directory.

## Command line usage for keyboard_service.py only
```bash
  -h, --help                        show this help message and exit
  --set_color SET_COLOR             Supported Colors: BLACK, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE
  --set_brightness SET_BRIGHTNESS   Any integer between 0-200.
  --get_color                       Returns current color.
  --get_brightness                  Returns current brightness.
  --skip_config_check               Skip config file check.
```
## Example
`sudo ./keyboard_service.py --set_color cyan --set_brightness 120`


## Note
This script needs root permission to work.

## Special note about XMG Core
To change color and brightness in Linux you need the [tuxedo-keyboard](https://github.com/tuxedocomputers/tuxedo-keyboard) kernel module. 
The Tuxedo Polaris and XMG Core got the same hardware, however both got a different firmware and the original tuxedo-keyboard kernel module
checks the board name.

To use the kernel module you have to compile your own module and add your device to the list of supported laptops. 

[Check out my branch of the kernel module](https://github.com/corus87/tuxedo-keyboard/blob/fbf0b2ed79af0a11805e53a2fb7d2bc89b83a04f/src/uniwill_keyboard.h#L458) with added support for the XMG Core 15.

You can get your board name by running `cat /sys/class/dmi/id/board_name`, on the XMG Core 15 E21 the output is `GK5NxxO M20`. 

