from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import pyautogui
import time
from selenium.webdriver.common.keys import Keys

Direction = '2'

role = 'All'
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

def total_Out(c,driver):    
    every = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["+str(c)+"]/td[6]/input")
    comments = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["+str(c)+"]/td[8]/p[2]/input")
    if ((comments.get_attribute("value")) == 'FULL SHIFT'):
        every.clear()
        every.send_keys("17:00")
    elif ((comments.get_attribute("value")) == ""):
        time.sleep(0.001)
    elif ((comments.get_attribute("value")) == '7-10PM'):
        every.clear()
        every.send_keys("17:00")
    else:
        time.sleep(0.001)


if(role == 'All'):
    for i in range(1,number+1):
        if(Direction == '2'):
            total_Out(i,driver)
    print("Number complete: ")
    print(i)

        
save = driver.find_element_by_id("btnSave")
save.click()
time.sleep(1)
save.send_keys(Keys.ENTER)
time.sleep(1)
driver.quit()
print("Completed Successfully")

        


    





