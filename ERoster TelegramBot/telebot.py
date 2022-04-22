import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from threading import Thread
from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import pyautogui
import time
import datetime
import xlrd

variable =  True


welcome_message  = """
Hello to auto adjust eroster
================================================
Type " /cphca "" /cpnurse" " /cpvacc "to check point AM shift to 1100-1200

Type " /cpall " to checkpoint all 

Type " /coamvacc " to adjust all AM shift vaccinator to 17:00

Type " /coamhca " to adjust all AM shift HCA to 18:00

Type " /coamnurse " to adjust all AM shfit Nurse to 17:00

Type " /coall " to adjust all AM shfit

Type " /adjustshifttiming " to adjust all AM FULL SHIFTS to 17:00 CO

================================================

Type " /eightam " to adjust all to 0800 and save

Type " /sixpm " to adjust all to 1800 and save

Type " /tenpm " to adjust all to 2200 and save

================================================

Type " /coallambutton " to press all CO AM buttons

Type " /coallpmbutton " to press all CO PM buttons


===============================================
Type " /shutoff " to close the bot server
YOU CANNOT TURN ON THE BOT REMOTELY
===============================================
/main

"""

user_message = """
Hidden user
===================
/CIMyselfAM
/CIMyselfPM
/listout
/listin
/main
===================
"""
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
       
    if msg['text'] == '/help':
        bot.sendMessage(chat_id,welcome_message)

    elif msg['text'] == '/main':
        bot.sendMessage(chat_id,user_message)

    elif  msg['text'] == '/eightam':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Changing all to 08:00, hold on...")
        start(chat_id)
    elif  msg['text'] == '/sixpm':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Changing all to 18:00, hold on...")
        pmci(chat_id)
    elif  msg['text'] == '/tenpm':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Changing all to 22:00, hold on...")
        pmco(chat_id)
    elif  msg['text'] == '/cpall':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkpoint ALL AM Shift 11AM/12PM, hold on... Takes around 5 mins")
        cpall(chat_id)
    elif  msg['text'] == '/cphca':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkpoint HCA AM Shift 11AM/12PM, hold on... Takes around 2 mins")
        cphca(chat_id)
    elif  msg['text'] == '/cpvacc':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkpoint Vaccinator AM Shift 11AM/12PM, hold on... Takes around 2 mins")
        cpvacc(chat_id)
    elif  msg['text'] == '/cpnurse':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkpoint Nurse AM Shift 11AM/12PM, hold on... Takes around 2 mins")
        cpnurse(chat_id)
    elif  msg['text'] == '/coamvacc':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout Vaccinators AM shift to 17:00, hold on...")
        co_vacc(chat_id)
    elif  msg['text'] == '/coamhca':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout HCA AM shift to 18:00, hold on...")
        co_hca(chat_id)
    elif  msg['text'] == '/coamnurse':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout Nurse AM shift to 17:00, hold on...")
        co_nurse(chat_id)
    elif  msg['text'] == '/coall':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout All AM shift to timing, hold on...")
        co_all(chat_id)
        shiftspecial(chat_id)
    elif  msg['text'] == '/coallambutton':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout All AM")
        co_allam(chat_id)
    elif  msg['text'] == '/coallpmbutton':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Checkout All PM")
        co_allpm(chat_id)
    elif  msg['text'] == '/adjustshifttiming':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence: Adjusting FULL SHIFT etc.checkout timing ")
        progress(chat_id)
        shiftspecial(chat_id)
        bot.sendMessage(chat_id,"Complete")

        
    elif msg['text'] == '/CIMyselfAM':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence...")
        exec(open("CIMeAM.py").read())
        bot.sendMessage(chat_id,"Completed Successfully")
        
    elif msg['text'] == '/listout':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence...")
        listoutg(chat_id)
        bot.sendMessage(chat_id,"Completed Successfully")
        
    elif msg['text'] == '/listin':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence...")
        listing(chat_id)
        bot.sendMessage(chat_id,"Completed Successfully") 
    elif msg['text'] == '/CIMyselfPM':
        bot.sendMessage(chat_id,msg['text'])
        bot.sendMessage(chat_id,"Initializing Sequence...")
        exec(open("CIMePM.py").read())
        bot.sendMessage(chat_id,"Completed Successfully") 
    elif msg['text'] == '/shutoff':
        bot.sendMessage(chat_id,"shutting down the bot...bye")
        pyautogui.hotkey('ctrl','c')
        quit()
        
    else:
        bot.sendMessage(chat_id,"I dont understand. Type /help for more info")
def progress(chat_id):
    bot.sendMessage(chat_id,"#")
    bot.sendMessage(chat_id,"##")
    bot.sendMessage(chat_id,"###")
    bot.sendMessage(chat_id,"Working...")
    

def start(chat_id):
    exec(open("AM_to_0800.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")
    
def shiftspecial(chat_id):
    exec(open("AdjustShiftTiming.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")
  
def co_allam(chat_id):
    exec(open("COAllam.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")
 
def co_allpm(chat_id):
    exec(open("COAllpm.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def cphca(chat_id):
    exec(open("CPHCA.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def cpall(chat_id):
    exec(open("CPHCA.py").read())
    print("HCA Complete...")
    bot.sendMessage(chat_id,"HCA Complete")
    exec(open("CPVacc.py").read())
    print("Vaccinator Complete...")
    bot.sendMessage(chat_id,"Vaccinator Complete")
    exec(open("CPNurse.py").read())
    print("Nurse Complete")
    bot.sendMessage(chat_id,"Nurse Complete")
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def cpvacc(chat_id):
    exec(open("CPVacc.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def cpnurse(chat_id):
    exec(open("CPNurse.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")
    
def pmci(chat_id):
    exec(open("PM_to_1800.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def pmco(chat_id):
    exec(open("PM_to_2200.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def co_vacc(chat_id):
    exec(open("CO_Vacc_17.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def co_hca(chat_id):
    exec(open("CO_HCA_18.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def co_all(chat_id):
    exec(open("CO_HCA_18.py").read())
    print("HCA Complete...")
    bot.sendMessage(chat_id,"HCA Complete")
    exec(open("CO_Vacc_17.py").read())
    print("Vaccinator Complete...")
    bot.sendMessage(chat_id,"Vaccinator Complete")
    exec(open("CO_Nurse_17.py").read())
    print("Nurse Complete...")
    bot.sendMessage(chat_id,"Nurse Complete")
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def co_nurse(chat_id):
    exec(open("CO_Nurse_17.py").read())
    print("Complete")
    bot.sendMessage(chat_id,"Completed Successfully")

def total(c,chat_id,driver):    
    every = driver.find_element_by_xpath("(//*[@name='item.TimeOutTitle'])["+str(c)+"]")
    word = every.get_attribute("value")
    print(word)
    worded = format(str(word))
    bot.sendMessage(chat_id,worded)
    
def listoutg(chat_id):
    driver = webdriver.Chrome(r'C:\chromedriver')
    driver.get("https://abs.rafflesmedical.com.sg/eroster/Account/Logout")
    print(driver.title)
    #login here
    driver.find_element_by_id("editorUserName").send_keys("HCA-91090053")
    driver.find_element_by_id("password").send_keys("098890ang")
    ddelement = Select(driver.find_element_by_id("ddlClusters"))
    ddelement.select_by_index(13)
    driver.find_element_by_css_selector(".btn.btn-info").click()
    #go to attendance list
    driver.find_element_by_link_text("Attendance").click()
    driver.find_element_by_link_text("Attendance List").click()

    number = driver.find_element_by_name("btnFilterTotalBooked").text
    number = number[13:]
    number = int(number)

    for i in range(1,number+1):
        total(i,chat_id,driver)
    driver.quit()
    print("Task complete")

def totalin(c,chat_id,driver):    
    every = driver.find_element_by_xpath("(//*[@name='item.TimeInTitle'])["+str(c)+"]")
    word = every.get_attribute("value")
    print(word)
    worded = format(str(word))
    bot.sendMessage(chat_id,worded)
    
def listing(chat_id):
    driver = webdriver.Chrome(r'C:\chromedriver')
    driver.get("https://abs.rafflesmedical.com.sg/eroster/Account/Logout")
    print(driver.title)
    #login here
    driver.find_element_by_id("editorUserName").send_keys("HCA-91090053")
    driver.find_element_by_id("password").send_keys("098890ang")
    ddelement = Select(driver.find_element_by_id("ddlClusters"))
    ddelement.select_by_index(13)
    driver.find_element_by_css_selector(".btn.btn-info").click()
    #go to attendance list
    driver.find_element_by_link_text("Attendance").click()
    driver.find_element_by_link_text("Attendance List").click()

    number = driver.find_element_by_name("btnFilterTotalBooked").text
    number = number[13:]
    number = int(number)

    for i in range(1,number+1):
        totalin(i,chat_id,driver)
    driver.quit()
    print("Task complete")
    
bot = telepot.Bot('5132738650:AAHFuF0jmGh_d0l7sEz_eUZEiFHBjZE08qI')
MessageLoop(bot,handle).run_as_thread()
while(1):
    time.sleep(5)
    print("ready")
