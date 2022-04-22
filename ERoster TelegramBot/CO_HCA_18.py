from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import pyautogui
import time
Direction = '2'

role = 'HCA'
if(role == 'HCA'):
    role = 'HCA'
elif(role == 'Vaccinator'):
    role = 'Vaccinator'
elif(role == 'Nurse'):
    role = 'Nurse'
elif(role == 'All'):
    role = 'All'
shift = 'AM'
if(shift == 'AM'):
    shift = '1'
elif(shift == 'PM'):
    shift = '2'

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
ddsession.select_by_index(shift)
driver.find_element_by_id("btnSearch").click()

number = driver.find_element_by_name("btnFilterTotalBooked").text
number = number[13:]
number = int(number)


def checkout(c,driver,direction,role):
    try:
       every = driver.find_element_by_xpath("(//*[@name='item.TimeOutTitle'])["+str(c)+"]")
       
       timing = every.get_attribute("value")
       hours = timing[:2]
       mins = timing[3:]
       hr = int(hours)
       min = int(mins)
       #print(f"{hours} and {mins}")
       if ((hr >= 17 and min >= 40) or hr >= 18):
           role = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["+str(c)+"]/td[2]/p[3]/b")
           id = role.text
           print(id)
           if id == 'HCA':
               role.click()       
               pyautogui.press('tab',7)
               pyautogui.press('backspace',1)
               pyautogui.typewrite(''+str("18:00"))

    except:
        return

   
if 1:
    for i in range(0,number):
        checkout(i,driver,Direction,role)
        print("Completed ")
        print(i+1)


driver.find_element_by_id("btnSave").click()
time.sleep(0.5)
print("Saved")
pyautogui.press('enter',1)
time.sleep(0.5)
#driver.quit()
print("Task complete")


