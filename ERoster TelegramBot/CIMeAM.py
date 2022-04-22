from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import pyautogui

function = 1

driver = webdriver.Chrome(r'C:\chromedriver.exe')
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
ddsession.select_by_index('1')
driver.find_element_by_id("btnSearch").click()

def checkout(i,driver):
    vacc = driver.find_element_by_xpath("// p[contains(text(),'Eugene Ang')]")
    vacc.click()
    pyautogui.press('tab',i)
    pyautogui.press('enter',4,0.5)


checkout(1,driver)

driver.quit()


