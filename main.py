import keyboard
import threading
import time
import win32gui
import win32process
import win32api
import win32con
import key_dict
import pyautogui

target_window_title = "GUI Name"
shouldStop = False


def enable():
    global shouldStop
    shouldStop = False
    t = threading.Thread(target=execute)
    t.start()


def disable():
    global shouldStop
    shouldStop = True


def execute():
    while not shouldStop:
        game_window = win32gui.FindWindow(None, target_window_title)
        if game_window > 0:
            remote_thread, _ = win32process.GetWindowThreadProcessId(game_window)
            win32process.AttachThreadInput(win32api.GetCurrentThreadId(), remote_thread, True)
            
            # Check if the window handle is still valid
            if win32gui.IsWindow(game_window):
                win32gui.SetForegroundWindow(game_window)
                
                pyautogui.press('1', presses=1, interval=0.0)
                pyautogui.press('NUM4', presses=1, interval=0.0)
                pyautogui.press('NUM2', presses=1, interval=0.0)
                pyautogui.press('2', presses=1, interval=0.0)
                pyautogui.press('3', presses=1, interval=0.0)
                pyautogui.press('4', presses=1, interval=0.0)
                pyautogui.press('NUM1', presses=1, interval=0.0)
                pyautogui.press('1', presses=1, interval=0.0)
                pyautogui.press('2', presses=1, interval=0.0)
                pyautogui.press('3', presses=1, interval=0.0)
                pyautogui.press('4', presses=1, interval=0.0)
                pyautogui.press('NUM5', presses=1, interval=0.0)
                pyautogui.press('NUM1', presses=1, interval=0.0)
                pyautogui.press('1', presses=1, interval=0.0)
                pyautogui.press('2', presses=1, interval=0.0)
                pyautogui.press('3', presses=1, interval=0.0)
                pyautogui.press('4', presses=1, interval=0.0)
                pyautogui.press('NUM1', presses=1, interval=0.0)
                pyautogui.press('NUM3', presses=1, interval=0.0)
               
            win32process.AttachThreadInput(win32api.GetCurrentThreadId(), remote_thread, False)
        #time.sleep(0.001)



def doKeyPress(key):
    pyautogui.press(key)
    

# Check for F1 key press and F2 key press events to control the key press simulation
keyboard.on_press_key("F1", lambda _: enable())
keyboard.on_press_key("F2", lambda _: disable())

# Keep the program running
while True:
    pass
