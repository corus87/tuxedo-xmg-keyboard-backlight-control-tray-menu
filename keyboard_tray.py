#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QDialog, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread
from time import sleep
import subprocess
import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CheckCurrentStates(QThread):
    def __init__(self, main):
        super(CheckCurrentStates,self).__init__()
        self.main = main

    def run(self):
        current_color = None
        current_brightness = None
        display_dimmed = False
        while True:
            if not display_dimmed:
                color, brightness = self.main.getStates()
                if color != current_color or brightness != current_brightness:
                    current_color = color
                    current_brightness = brightness
                    self.main.updateMenu(color=color, brightness=brightness)

                if self.main.getDisplayBrightness() == "Off":
                    self.main.setBrightness(0)
                    display_dimmed = True
            else:
                if self.main.getDisplayBrightness() == "On":
                    self.main.setBrightness(current_brightness)
                    display_dimmed = False
            sleep(1)

class KeyboardColor(QSystemTrayIcon):
    def __init__(self):
        super().__init__()  
        main_menu = QMenu()

        self.color_menu = main_menu.addMenu("Farbe")
        self.brightness_menu = main_menu.addMenu("Helligkeit")
        self.addColorMenu()
        self.addBrightnessMenu()
        
        check = CheckCurrentStates(self)
        check.start()

        main_menu.addSeparator()

        self.exit_button = QAction("Beenden")
        self.exit_button.triggered.connect(app.quit)
        
        main_menu.addAction(self.exit_button)
        
        color, brightness = self.getStates()

        if brightness < 0:
            self.brightness_save_state = brightness
        else:
            self.setIcon(QIcon("keyboard-off.png"))
            self.brightness_save_state = 30

        self.setIcon(QIcon("keyboard-on.png"))
        self.setVisible(True)
        self.setToolTip("Keyboard-backlight")
        self.setContextMenu(main_menu)
        self.activated.connect(self.on_click)

    def on_click(self):
        cl, brightness = self.getStates()
        if brightness > 0:
            self.brightness_save_state = brightness
            self.setBrightness(0)
        else:
            self.setBrightness(self.brightness_save_state)
            
    def updateMenu(self, color=None, brightness=None):
        if color:
            self.set_red.setChecked(True if color == "RED" else False)
            self.set_red.setEnabled(False if color == "RED" else True)
            self.set_green.setChecked(True if color == "GREEN" else False)
            self.set_green.setEnabled(False if color == "GREEN" else True)
            self.set_blue.setChecked(True if color == "BLUE" else False)
            self.set_blue.setEnabled(False if color == "BLUE" else True)
            self.set_yellow.setChecked(True if color == "YELLOW" else False)
            self.set_yellow.setEnabled(False if color == "YELLOW" else True)
            self.set_magenta.setChecked(True if color == "MAGENTA" else False)
            self.set_magenta.setEnabled(False if color == "MAGENTA" else True)
            self.set_cyan.setChecked(True if color == "CYAN" else False)
            self.set_cyan.setEnabled(False if color == "CYAN" else True)
            self.set_white.setChecked(True if color == "WHITE" else False)
            self.set_white.setEnabled(False if color == "WHITE" else True)

        if brightness is not None:
            if brightness == 0:
                self.setIcon(QIcon("keyboard-off.png"))
            else:
                self.setIcon(QIcon("keyboard-on.png"))

            self.set_zero.setChecked(True if brightness == 0 else False)
            self.set_zero.setEnabled(False if brightness == 0 else True)
            self.set_ten.setChecked(True if brightness == 10 else False)
            self.set_ten.setEnabled(False if brightness == 10 else True)
            self.set_twenty.setChecked(True if brightness == 20 else False)
            self.set_twenty.setEnabled(False if brightness == 20 else True)
            self.set_thirty.setChecked(True if brightness == 30 else False)
            self.set_thirty.setEnabled(False if brightness == 30 else True)
            self.set_fourty.setChecked(True if brightness == 40 else False)
            self.set_fourty.setEnabled(False if brightness == 40 else True)
            self.set_fifty.setChecked(True if brightness == 50 else False)
            self.set_fifty.setEnabled(False if brightness == 50 else True)
            self.set_sixty.setChecked(True if brightness == 60 else False) 
            self.set_sixty.setEnabled(False if brightness == 60 else True) 
            self.set_seventy.setChecked(True if brightness == 70 else False)
            self.set_seventy.setEnabled(False if brightness == 70 else True)
            self.set_eighty.setChecked(True if brightness == 80 else False)
            self.set_eighty.setEnabled(False if brightness == 80 else True)
            self.set_ninety.setChecked(True if brightness == 90 else False)
            self.set_ninety.setEnabled(False if brightness == 90 else True)
            self.set_hundred.setChecked(True if brightness == 100 else False)
            self.set_hundred.setEnabled(False if brightness == 100 else True)

    def addColorMenu(self):
        self.set_red = QAction("Rot")
        self.set_red.setCheckable(True)
        self.set_red.triggered.connect(lambda: self.setColor("red"))
        self.set_green = QAction("Grün")
        self.set_green.setCheckable(True)
        self.set_green.triggered.connect(lambda: self.setColor("green"))
        self.set_blue = QAction("Blau")
        self.set_blue.setCheckable(True)
        self.set_blue.triggered.connect(lambda: self.setColor("blue"))
        self.set_yellow = QAction("Gelb")
        self.set_yellow.setCheckable(True)
        self.set_yellow.triggered.connect(lambda: self.setColor("yellow"))
        self.set_magenta = QAction("Magenta")
        self.set_magenta.setCheckable(True)
        self.set_magenta.triggered.connect(lambda: self.setColor("magenta"))
        self.set_cyan = QAction("Cyan")
        self.set_cyan.setCheckable(True)
        self.set_cyan.triggered.connect(lambda: self.setColor("cyan"))
        self.set_white = QAction("Weiß")
        self.set_white.setCheckable(True)
        self.set_white.triggered.connect(lambda: self.setColor("white"))
        self.color_menu.addAction(self.set_red)
        self.color_menu.addAction(self.set_green)
        self.color_menu.addAction(self.set_blue)
        self.color_menu.addAction(self.set_yellow)
        self.color_menu.addAction(self.set_magenta)
        self.color_menu.addAction(self.set_cyan)
        self.color_menu.addAction(self.set_white)

    def addBrightnessMenu(self):
        self.set_zero = QAction("0%")
        self.set_zero.setCheckable(True)
        self.set_zero.triggered.connect(lambda: self.setBrightness(0))
        self.set_ten = QAction("10%")
        self.set_ten.setCheckable(True)
        self.set_ten.triggered.connect(lambda: self.setBrightness(10))
        self.set_twenty = QAction("20%")
        self.set_twenty.setCheckable(True)
        self.set_twenty.triggered.connect(lambda: self.setBrightness(20))
        self.set_thirty = QAction("30%")
        self.set_thirty.setCheckable(True)
        self.set_thirty.triggered.connect(lambda: self.setBrightness(30))
        self.set_fourty = QAction("40%")
        self.set_fourty.setCheckable(True)
        self.set_fourty.triggered.connect(lambda: self.setBrightness(40))
        self.set_fifty = QAction("50%")
        self.set_fifty.setCheckable(True)
        self.set_fifty.triggered.connect(lambda: self.setBrightness(50))
        self.set_sixty = QAction("60%")
        self.set_sixty.setCheckable(True)
        self.set_sixty.triggered.connect(lambda: self.setBrightness(60))
        self.set_seventy = QAction("70%")
        self.set_seventy.setCheckable(True)
        self.set_seventy.triggered.connect(lambda: self.setBrightness(70))
        self.set_eighty = QAction("80%")
        self.set_eighty.setCheckable(True)
        self.set_eighty.triggered.connect(lambda: self.setBrightness(80))
        self.set_ninety = QAction("90%")
        self.set_ninety.setCheckable(True)
        self.set_ninety.triggered.connect(lambda: self.setBrightness(90))
        self.set_hundred = QAction("100%")
        self.set_hundred.setCheckable(True)
        self.set_hundred.triggered.connect(lambda: self.setBrightness(100))
        self.brightness_menu.addAction(self.set_zero)
        self.brightness_menu.addAction(self.set_ten)
        self.brightness_menu.addAction(self.set_twenty)
        self.brightness_menu.addAction(self.set_thirty)
        self.brightness_menu.addAction(self.set_fourty)
        self.brightness_menu.addAction(self.set_fifty)
        self.brightness_menu.addAction(self.set_sixty)
        self.brightness_menu.addAction(self.set_seventy)
        self.brightness_menu.addAction(self.set_eighty)
        self.brightness_menu.addAction(self.set_ninety)
        self.brightness_menu.addAction(self.set_hundred)

    def setBrightness(self, brightness):
        cĺ, cb = self.getStates()
        to_set = brightness * 2
        current_brightness = cb * 2

        # Fade in steps 20 
        if to_set > current_brightness:
            for i in range(current_brightness, to_set, 20):
                subprocess.call(["sudo", "./keyboard_service.py", "--set_brightness", str(i), "--skip_config_check"])

        else:
            for i in range(current_brightness, to_set, -20):
                subprocess.call(["sudo", "./keyboard_service.py", "--set_brightness", str(i), "--skip_config_check"])

        # Set final brightness
        subprocess.call(["sudo", "./keyboard_service.py", "--set_brightness", str(to_set), "--skip_config_check"])
        
    def setColor(self, color):
        subprocess.call(["sudo", "./keyboard_service.py", "--set_color", color])

    def getStates(self):
        cl = subprocess.run(["./keyboard_service.py", "--get_color", "--skip_config_check"], stdout=subprocess.PIPE)
        color = cl.stdout.decode("UTF-8").strip()

        bs = subprocess.run(["./keyboard_service.py", "--get_brightness", "--skip_config_check"], stdout=subprocess.PIPE)
        brightness = int(bs.stdout.decode("UTF-8")) // 2

        return color, round(brightness, -1)

    def getDisplayBrightness(self):
        cl = subprocess.run(["xset", "q"], stdout=subprocess.PIPE)
        return re.search('Monitor is (.*)', cl.stdout.decode("UTF-8")).group(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    KeyboardColor()
    sys.exit(app.exec_())
    
