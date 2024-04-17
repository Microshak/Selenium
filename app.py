from selenium import webdriver
#from seleniumwire import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import table as Table
import db as DB
import time



options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

DB.dbinit()

driver.get("http://www.microshak.com")



start = 1
for id in range(start,100):

    
    driver.get("http://www.microshak.com?micro_id=" + str(id))
    
    

    account = {}
    driver.implicitly_wait(1.5)
    
    

    driver.find_element(By.XPATH,'//select').click()

    account = Table.getTable("microtable", driver)
    
    

    ddl = driver.find_element(By.ID, 'clientDDL')
    select = Select(ddl)
    txt = select.first_selected_option

    account["Client"] = txt.text
    account["AccountType"] = Select(driver.find_element(By.ID, 'asdf')).first_selected_option.text
   
    account["AccountNum"] = driver.find_element(by=By.ID, value="abn").get_attribute('value')



    if(start == id):
        print("🔥")
        DB.recreateTable("microGeneral", account)
    DB.insertTable("microGeneral", account,id)
    


    
driver.quit()












