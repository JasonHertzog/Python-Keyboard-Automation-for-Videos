# documentation used: https://github.com/boppreh/keyboard#api
from pynput.keyboard import Key, Controller
import keyboard

# This is used to press enter with pynput
enterboard = Controller() 

the_script = ['Test', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5']
i = 0
keyboard.wait('shift')
while i < len(the_script):
    keyboard.write(the_script[i], delay=0.03)
    enterboard.press(Key.enter)
    enterboard.release(Key.enter)
    i += 1
    keyboard.wait('shift')