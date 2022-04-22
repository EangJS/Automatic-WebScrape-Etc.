from selenium import webdriver
import pyautogui
import time

Vials_transferred_Out_to_LVT_HVT = input("Vials Transfer Out to LVT/HVT ")
Vaccine_Used_On_Clients = input("Vials Used On Clients ")
Number_of_Vaccine_Remaining = input("Vials Remaining ")
Number_of_Vaccine_Wasted = '0'
Number_of_Vaccine_Batches = input("Batches Remaining ")

Batch_1_quantity = input("Batch 1 Quantity ")
Batch_1_date = input("Batch 1 Date ")

Batch_2_quantity = input("Batch 2 Quantity ")
Batch_2_date = input("Batch 2 Date ")

Batch_3_quantity = input("Batch 3 Quantity ")
Batch_3_date = input("Batch 3 Date ")

Batch_4_quantity = input("Batch 4 Quantity ")
Batch_4_date = input("Batch 4 Date ")

Number_of_Vials_transferred_Out = Vials_transferred_Out_to_LVT_HVT
Number_of_Vials_transferred_in = '0'
Number_of_Vials_Quarantined = '0'
Vials_planned = '0'


Number_of_external_scheduled = input("External Scheduled ")
Dose_1 = input("Dose 1 ")
Dose_2 = input("Dose 2 ")
Dose_B_3 = input("Dose B/3 ")
Dose_B2 = input("Dose B2")
Defer = input("Defer ")
No_show = input("No Show ")
Walk_in = input("Walk in ")


Allergist = '0'

driver = webdriver.Chrome(r'C:\Program Files\Formfiller\chromedriver.exe')
#driver = webdriver.Chrome(r'C:\Users\eugen\chromedriver.exe')
driver.get("https://form.gov.sg/#!/5fe2ea9272689300133ec545")
print(driver.title)

time.sleep(0.5)
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[2]/field-directive/div/text-field-component/div/div[1]/input").send_keys("Aileen How")

driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[3]/field-directive/div/text-field-component/div/div[1]/input").send_keys("760F")
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[4]/field-directive/div/email-field-component/div/verifiable-field-component/ng-transclude/div[1]/input").send_keys("how_aileen@rafflesmedical.com")
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[5]/field-directive/div/mobile-field-component/div/verifiable-field-component/ng-transclude/div[1]/div/input").send_keys('82926632')


driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[7]/field-directive/div/date-field-component/div/div[1]/div/input").click()
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[7]/field-directive/div/date-field-component/div/div[1]/div/div/ul/li[2]/button").click()

time.sleep(0.5)
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[9]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]").click()
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[11]/field-directive/div/dropdown-field-component/div/div[1]/div/div/div[1]/input").click()
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[11]/field-directive/div/dropdown-field-component/div/div[1]/div/div/div[2]/div/div/div[16]/div").click()

time.sleep(1)

driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[12]/field-directive/div/dropdown-field-component/div/div[1]/div/div/div[1]").click()
driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[12]/field-directive/div/dropdown-field-component/div/div[1]/div/div/div[2]/div/div/div[2]/div").click()


centre = driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[13]/field-directive/div/dropdown-field-component/div/div[1]/div/div/div[1]/input")
centre.click()
centre.send_keys("Teck Ghee CC")
time.sleep(0.5)
pyautogui.press('enter',1)


pyautogui.press('tab',2)
pyautogui.press('enter',1)
pyautogui.typewrite(str(Vials_transferred_Out_to_LVT_HVT))

pyautogui.press('tab',1)
pyautogui.press('enter',1)
pyautogui.typewrite(str(Vaccine_Used_On_Clients))

pyautogui.press('tab',1)
pyautogui.press('enter',1)
pyautogui.typewrite(str(Number_of_Vaccine_Remaining))

pyautogui.press('tab',1)
pyautogui.press('enter',1)
pyautogui.typewrite(str(Number_of_Vaccine_Wasted))

pyautogui.press('tab',1)
pyautogui.press('enter',1)
pyautogui.typewrite(str(Number_of_Vaccine_Batches))
time.sleep(0.5)
pyautogui.press('tab',1)
time.sleep(0.5)

def batch_func(set_num,set_date):
    pyautogui.press('tab',1)
    pyautogui.typewrite(str(set_num))
    pyautogui.press('tab',1)
    pyautogui.typewrite(str(set_date))
    

if(Number_of_Vaccine_Batches == '1'):
    batch_func(Batch_1_quantity,Batch_1_date)


if(Number_of_Vaccine_Batches == '2'):
    batch_func(Batch_1_quantity,Batch_1_date)
    pyautogui.press('tab',1)
    batch_func(Batch_2_quantity,Batch_2_date)

if(Number_of_Vaccine_Batches == '3'):
    batch_func(Batch_1_quantity,Batch_1_date)
    pyautogui.press('tab',1)
    batch_func(Batch_2_quantity,Batch_2_date)
    pyautogui.press('tab',1)
    batch_func(Batch_3_quantity,Batch_3_date)

if(Number_of_Vaccine_Batches == '4'):
    batch_func(Batch_1_quantity,Batch_1_date)
    pyautogui.press('tab',1)
    batch_func(Batch_2_quantity,Batch_2_date)
    pyautogui.press('tab',1)
    batch_func(Batch_3_quantity,Batch_3_date)
    pyautogui.press('tab',1)
    batch_func(Batch_4_quantity,Batch_4_date)

pyautogui.press('tab',2)
pyautogui.typewrite(Number_of_Vials_transferred_Out,0.2)
if(Vials_transferred_Out_to_LVT_HVT != '0'):
    pyautogui.press('tab',1)
    pyautogui.typewrite("HVT")
else:
    time.sleep(0.1)

pyautogui.press('tab',1)
pyautogui.typewrite(Number_of_Vials_transferred_in,0.2)

pyautogui.press('tab',1)
pyautogui.typewrite(Number_of_Vials_Quarantined,0.2)

pyautogui.press('tab',1)
pyautogui.typewrite(Vials_planned,0.2)
#pyautogui.press("pgdn",1)
batch = int(Number_of_Vaccine_Batches)
if(Number_of_Vials_transferred_Out == '0'):
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(25+ batch*3)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]").click()
else:
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(25 + batch*3 + 1)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]").click()
if(Number_of_Vials_transferred_Out == '0'):
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(27 + batch*3)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]").click()
else:
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(27 + batch*3 + 1)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]").click()
time.sleep(0.5)

pyautogui.press('tab',1)
pyautogui.typewrite(str(Number_of_external_scheduled))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Dose_1))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Dose_2))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Dose_B_3))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Dose_B2))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Defer))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(No_show))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Walk_in))

pyautogui.press('tab',1)
pyautogui.typewrite(''+str(Allergist))



if(Vials_transferred_Out_to_LVT_HVT != '0'):
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(38 + batch*3 + 1)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[2]").click()
    pyautogui.press('pgdn',1)
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(40 + batch*3 + 1)+"]/field-directive/div/checkbox-field-component/div/div[2]/div/div/label").click()
else:
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(38 + batch*3)+"]/field-directive/div/yes-no-field-component/div/div[2]/div/label[2]").click()
    pyautogui.press('pgdn',1)
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div["+str(40 + batch*3)+"]/field-directive/div/checkbox-field-component/div/div[2]/div/div/label").click()

time.sleep(1800)
driver.quit()
