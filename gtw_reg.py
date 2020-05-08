#GTW Register Bot
#Purpose: To take a CSV of GTW recipients and re-register them for another event.
#Author: Joe Anderson
#Date: 04/03/2020

from webbot import *
from os import path
import time
import csv
import sys

#Validate filepath
#------------------------
def getFilepath():
    valid = False

    while valid==False:
        io = input('Please enter a filepath for your CSV: \n')

        if path.exists(io):
            valid = True
        else:
            print('This is not a valid filepath')
            valid = False
    
    return io
#-------------

def getURL():
    io = input('Please enter a GoToWebinar ID: \n')
    url = "https://register.gotowebinar.com/register/" + str(io)
    return url
    

#Import CSV data
#--------------
def importCSV(filepath, url):
    web = Browser()
    
    with open(filepath) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            fn = row[0]
            ln = row[1]
            em = row[2]

            postData(fn, ln, em, url, web)
#---------------------------------

#Post CSV data to site
#----------------------------------------
def postData(firstname, lastname, email, site, web):

    web.go_to(site)
    time.sleep(5)
    web.type(firstname, into='firstname', clear=True, multiple=False, tag='input', id='registrant.firstName', classname='form-controlmaxCharLimit', css_selector='#registrant\.firstName', xpath='/html/body/div/div/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/div[1]/div[1]/input', loose_match=False)
    time.sleep(2)
    web.type(lastname, into='lastname', clear=True, multiple=False, tag='input', id='registrant.lastName', classname='form-controlmaxCharLimit', css_selector='#registrant\.lastName', xpath='/html/body/div/div/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/div[1]/div[2]/input', loose_match=False)
    time.sleep(2)
    web.type(email, into='email', clear=True, multiple=False, tag='input', id='registrant.email', classname='form-controlmaxCharLimit', css_selector='#registrant\.email', xpath='/html/body/div/div/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/div[2]/div/input', loose_match=False)
    time.sleep(2)
    web.click(text='Register', tag='button', id='registration.submit.button')
    time.sleep(2)
    web.close_current_tab
#-------------------------

#Main method
print()
print("GTW Register Bot")
print("Purpose: To take a CSV of GTW recipients and re-register them for another event.")
print("Author: Joe Anderson")
print("Date: 04/03/2020")

filepath = getFilepath()
url = getURL()
importCSV(filepath, url)
sys.exit()