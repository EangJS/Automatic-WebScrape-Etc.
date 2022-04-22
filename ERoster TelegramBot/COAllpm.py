from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import pyautogui


driver = webdriver.Chrome(r'C:\chromedriver')
driver.get("https://abs.rafflesmedical.com.sg/eroster/Account/Logout")
print(driver.title)
#login here
driver.find_element_by_id("editorUserName").send_keys("HCA-91090053")
driver.find_element_by_id("password").send_keys("098890ang")
ddelement = Select(driver.find_element_by_id("ddlClusters"))
ddelement.select_by_index('13')
driver.find_element_by_css_selector(".btn.btn-info").click()
#go to attendance list
driver.find_element_by_link_text("Attendance").click()
driver.find_element_by_link_text("Attendance List").click()

ddsession = Select(driver.find_element_by_class_name("ddlSession"))
ddsession.select_by_index(2)
driver.find_element_by_id("btnSearch").click()

driver.find_element_by_name("btnFilterTotalCheckedIn").click()
def checkout(i,driver):
    try:
        vacc = driver.find_element_by_xpath("(//*[@id='AttendanceList']/tbody/tr["+str(i)+"]/td[1])")
        vacc.click()
        pyautogui.press('tab',3)
        pyautogui.press('enter',3,0.2)
        time.sleep(1)
        print("Number complete: ")
        print(i)
    except:
        return
        
for i in range(1,50):
    checkout(i,driver)

driver.quit()
print("Completed Successfully")




    





#sign in
#driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["%s"]/td[2]/p[5]/button[1]' % i).click()
#driver.switch_to.alert.dismiss()
#sign in by monthly increment
#string = f'[id$=btnCI_6453{k}]'
#driver.find_element_by_css_selector(string).click()
