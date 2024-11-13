from transformers import pipeline
from pynput.keyboard import Key, Controller
import pyautogui
import time
import keyboard
simulate_key = Controller()
#if 'with keyboard' variable is 1 and 'with mouse' variable is 0 it will use the a/d button to rotate the camera of the game
#if 'with mouse' variable is 1 and 'with keyboard' variable is 0 it will use mouse to rotate the camera of the game
with_keyboard = 0
with_mouse = 1
option_detector = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32") #selecting the model

while True:
    screenshot = pyautogui.screenshot('screenshot.png')#getting screenshot
    image = 'screenshot.png' #selecting the screenshot
    options = ['should insult','should greet', 'should look left', 'should look right','should move backward','should move forward', 'should attack'] #ai's options


    results = option_detector(image, candidate_labels=options) #detects what is the 'best option' to do

    results_labels = [result['label'] for result in results]
    ai_choosen_action = results_labels[0]
    print(ai_choosen_action)


    #the actions that ai can do
    #if you want to add a action it recommended to add 'should' at the beginning
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
            pyautogui.moveRel(-500, 0)
    if results_labels[0] == 'should look right':
        if with_keyboard == 1:
            simulate_key.press('d')
            time.sleep(0.2)
            simulate_key.release('d')
        elif with_mouse == 1:
            pyautogui.moveRel(500, 0)
    if results_labels[0] == 'should attack':
        pyautogui.click()
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
