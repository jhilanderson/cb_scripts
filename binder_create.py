# CB Engagement Data Exporter
# Author: Joe Anderson
# Copyright (C) 2019
# Purpose: Export data from software that requires painfully tedious attention. This is a laughably unstable script.

import pyautogui, time
pyautogui.FAILSAFE= False
print("CB Engagement Data Exporter")
print("Author: Joe Anderson")
print("Copyright (C) 2019")
print('Press Ctrl-C to quit.')

#We ask the user how many binders there are and if they're finalized, which takes longer to process
final = input('Are these binders finalized? (Y or N please)')
binders = input('How many binders are you creating?')
binders = int(binders)
print("Now's the time to move your cursor before the work starts (10 sec).")
time.sleep(10)

#---------------------------------------------------------------------#
#There are two functions that can run, finalizedBinder and createBinder

#Run if the binders are finalized
def finalizedBinder(a):

#The cursor will need to begin at the top of list
#for y in binders
        pyautogui.scroll(3000)
        time.sleep(3)
        pyautogui.click(508, 106)

#Move the cursor down to the binder to create
        if a > 0:
            for z in range(y):
                pyautogui.press('down')

        pyautogui.press('apps')
        time.sleep(1)

#Navigate to create binder package
        for x in range(13):
            pyautogui.press('up')
            time.sleep(1)

#Click on create binder package button
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)

#Click OK to begin creating binder and confirm the creation
        pyautogui.press('enter')
        time.sleep(120)
        pyautogui.press('enter')

#----#
#Run if the binders are not finalized
def createBinder(b):

#The cursor will need to begin at the top of list
#for y in binders
        pyautogui.scroll(3000)
        time.sleep(3)
        pyautogui.click(508, 106)

#Move the cursor down to the binder to create
        if b > 0:
            for z in range(y):
                pyautogui.press('down')

        pyautogui.press('apps')
        time.sleep(1)

#Navigate to create binder package
        for x in range(13):
            pyautogui.press('up')
            time.sleep(1)

#Click on create binder package button
        pyautogui.press('enter')
        time.sleep(5)

#Click OK to begin creating binder and confirm the creation
        pyautogui.press('enter')
        time.sleep(60)
        pyautogui.press('enter')
#---------------------------------------------------------------------#

#This will run depending on how many binders the user has to process
if (final == 'y' or final == 'Y'):
    for y in range(binders):
        finalizedBinder(y)

elif (final == 'n' or final == 'N'):
    for y in range(binders):
        createBinder(y)
