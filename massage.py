import pyautogui
counter=20 # Counter = n 
while counter>0:
    pyautogui.typewrite("abc")
    pyautogui.press("enter")
    counter-=1
