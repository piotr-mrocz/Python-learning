#Zadanie21.
#Napisz program, który za pomocą pyautogui wysyła wiadomości
#Kocham Cię na messengerze.

import pyautogui
import time
import webbrowser as wb


wb.open("https://www.messenger.com/t/100000685519724")
while True:
    
    time.sleep(3)
    message = 'Kocham Cie'
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    break

