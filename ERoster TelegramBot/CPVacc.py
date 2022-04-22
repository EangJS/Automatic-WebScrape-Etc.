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
ddsession.select_by_index(1)
driver.find_element_by_id("btnSearch").click()
driver.find_element_by_name("btnFilterTotalBooked").click()



def cp(i,driver,role):
    try:
        time.sleep(1)
        vacc = driver.find_elements_by_xpath("// b[contains(text(),'"+str(role)+"')]")
        vacc[i].click()
        time.sleep(1)
        pyautogui.press('tab',8)
        pyautogui.press('enter',1)
        time.sleep(0.8)
        driver.find_element_by_id("CheckPoint").clear()
        driver.find_element_by_id("CheckPoint").send_keys("11:00:00")
        time.sleep(0.5)
        driver.find_element_by_id("btnAddCPC").click()    
        driver.find_element_by_id("CheckPoint").clear()
        driver.find_element_by_id("CheckPoint").send_keys("12:00:00")
        time.sleep(0.5)
        driver.find_element_by_id("btnAddCPC").click()
        driver.find_element_by_id("btnCancel").click()
        print("Number complete: ")
        print(i)
    except:
        return




for j in range(0,30):
    role = 'Vaccinator'
    cp(j,driver,role)




driver.quit()
print("Completed Successfully")




    





#sign in
#driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr["%s"]/td[2]/p[5]/button[1]' % i).click()
#driver.switch_to.alert.dismiss()
#sign in by monthly increment
#string = f'[id$=btnCI_6453{k}]'
#driver.find_element_by_css_selector(string).click()
