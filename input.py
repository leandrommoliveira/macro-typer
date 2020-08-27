from pynput.keyboard import Key, Controller
import time

class KeyboardInput:

    def type_string(self, value, delay=0):
        keyboard = Controller()
        time.sleep(delay)
        keyboard.type(value)
