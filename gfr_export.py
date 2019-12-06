# CB GFR Data Exporter
# Author: Joe Anderson
# Copyright (C) 2019
# Purpose: Export data from software that requires painfully tedious attention. This is a laughably unstable script.

import pyautogui, time

# Specifying cursor variables
counter = 0
xcord = 48
ycord = 226
pyautogui.FAILSAFE= True
print("CB GFR Data Exporter")
print("Author: Joe Anderson")
print("Copyright (C) 2019")
print('Press Ctrl-C to quit at any time.')
files = input('How many files are you exporting?')
files = int(files)
print("Please move your cursor away from the window. You have 20 seconds till the operation starts.")
time.sleep(5)

#Functions used to export data
#----------------------------------------#

#This moves the cursor to the specified data on the page by passing in the starting coordinates and the item counter
def exportGFR(a, b, c):

    #Move cursor to element
    pyautogui.moveTo(a, b)
    time.sleep(1.5)
    #Click on the element
    pyautogui.click()
    time.sleep(1.5)


    # Right-click on element
    pyautogui.rightClick()
    time.sleep(2)

    # This will determine where the cursor will end up to click on export
    if (c < 7):
        pyautogui.moveRel(25,235)
    if (c == 7):
        pyautogui.moveRel(20,5)
    if (c == 8):
        pyautogui.moveRel(16,-30)
    elif (c > 8):
        pyautogui.moveRel(23,-55)

    # Click export
    time.sleep(5)
    pyautogui.click()

    # Navigate to the save button
    time.sleep(1.5)
    pyautogui.moveTo(1298, 1016)
    time.sleep(2)
    pyautogui.click()
    time.sleep(3)

#Navigates the cursor to the next page to process more data
def nextPage():
    pyautogui.moveTo(1773, 160)
    time.sleep(5)
    pyautogui.click(1773, 160)
    time.sleep(5)

#Sets the y coordinates for the next item in the list
def nextItem(b, c):
    next = (26.8*c)+b
    return next

#---------#
#Running the script
for z in range(files):
    if (counter >= 20):
        counter = 0
        nextPage()
    x = xcord
    y = nextItem(ycord, counter)
    exportGFR(x,y,counter)
    counter = counter+1