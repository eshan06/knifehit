import pyautogui
import keyboard
import time
import win32api, win32con



def click(x, y):
    win32api.SetCursorPos( (x,y) )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) # delay before clicking 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

	'''
	=======================
	In the code below I use specific coordinates to check for color
	These coordinates may vary based on your screen size and website you are playing knife hit on
	Use the code below to find the color of the background and position you want to use

	When you use the code you will a tuple with values in it for the background color in rgb
	Replace the variable bgcolor with the first value in the tuple

	Code:

	pyautogui.displayMousePosition()

	=======================
	'''

    x = 1520
    y = 537
    x2 = 1320
    y2 = 537
    bgcolor = 4
    # Both checks are to make sure that the color of the knife is not nearby and the program is ready to shoot
    if pyautogui.pixel(1520, 537) [0] == bgcolor and pyautogui.pixel(1320, 537) [0] == bgcolor: # This checks the color at the coordinates
        click(x=1500, y=500) # Move to the coordinates then left click (make sure this coordinate is on your tab with knife hit)