from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import pyautogui
import time
from selenium.webdriver.common.by import By


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

ddsession = Select(driver.find_element_by_class_name("ddlSession"))
ddsession.select_by_index(2) #PM
driver.find_element_by_id("btnSearch").click()

#driver.find_element_by_name("btnFilterTotalCheckedIn").click()

number = driver.find_element_by_name("btnFilterTotalBooked").text
number = number[13:]
number = int(number)

def total_in(c,driver):
    every = driver.find_element_by_xpath("(//*[@name='item.TimeInTitle'])["+str(c)+"]")
    comments = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["+str(c)+"]/td[8]/p[2]/input")
    intime = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["+str(c)+"]/td[5]/input").get_attribute("value")
    min = intime[3:]
    hr = intime[:2]
    min = int(min)
    hr = int(hr)
    if((hr >= 18 and min >=5) or hr >=19) :
       comments.send_keys(" Late @ ")
       comments.send_keys(intime)
       return
    every.clear()
    every.send_keys("18:00")



    
for i in range(1,number+1):
    
    total_in(i,driver)
    print("Completed: ")
    print(i)
        



driver.find_element_by_id("btnSave").click()
time.sleep(0.5)
print("Saved")
pyautogui.press('enter',1)
time.sleep(0.5)
driver.quit()
print("Task complete")

