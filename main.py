from transformers import pipeline
from pynput.keyboard import Key, Controller
import pyautogui
import time
import keyboard
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
simulate_key = Controller()
def move_mouse_raw(dx, dy):
    """Moves the mouse using raw input (relative movement)."""
    ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)

with_keyboard = 0
with_mouse = 1
option_detector = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32") 
print('ai starting in 1 second')
time.sleep(1)
while True:
    screenshot = pyautogui.screenshot('screenshot.png')
    image = 'screenshot.png' 
    options = ['should look left', 'should look right','should move backward','should move forward'] #ai's options


    results = option_detector(image, candidate_labels=options) 

    results_labels = [result['label'] for result in results]
    ai_choosen_action = results_labels[0]
    print(ai_choosen_action)
    

    if results_labels[0] == 'should move forward':
        simulate_key.press('w')
        time.sleep(0.2)
        simulate_key.release('w')
    if results_labels[0] == 'should move backward':
        simulate_key.press('s')
        time.sleep(0.2)
        simulate_key.release('s')
    if results_labels[0] == 'should look left':
        if with_keyboard == 1:
            simulate_key.press('a')
            time.sleep(0.2)
            simulate_key.release('a')
        elif with_mouse == 1:
            move_mouse_raw(-250, 0)
    if results_labels[0] == 'should look right':
        if with_keyboard == 1:
            simulate_key.press('d')
            time.sleep(0.2)
            simulate_key.release('d')
        elif with_mouse == 1:
            move_mouse_raw(250, 0)
    if results_labels[0] == 'attack':
        pyautogui.click()
    else:
        pass
    if results_labels[0] == 'should greet':
        pyautogui.press('y')
        pyautogui.write('hello there!')
        simulate_key.press(Key.enter)
        simulate_key.release(Key.enter)
    if results_labels[0] == 'should insult':
        pyautogui.press('y')
        pyautogui.write('your ugly.')
        simulate_key.press(Key.enter)
        simulate_key.release(Key.enter)
    if keyboard.is_pressed('v'):
        if keyboard.is_pressed('b'):
            break
