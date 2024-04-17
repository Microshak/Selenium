from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


def getTable(tablename, driver):

    rows = driver.find_elements(By.XPATH,"//*[@id='"+tablename+"']/tbody/tr")
    rowLen = len(rows)
    title = "" 
    value = ""
    data = {}
    for x in range(0,rowLen):
        row = driver.find_elements(By.XPATH,"//*[@id='"+tablename+"']/tbody/tr["+str(x)+"]/td")
        for y in range(1,len(row) + 1):

            celltype = y % 2
            cell = driver.find_elements(By.XPATH,"//*[@id='"+tablename+"']/tbody/tr["+str(x)+"]/td["+str(y)+"]")
            
        
            if celltype == 0:
                input = driver.find_elements(By.XPATH,"//*[@id='"+tablename+"']/tbody/tr["+str(x)+"]/td["+str(y)+"]/input")
                value = [elm.get_attribute('value') for elm in input]
                
                if len(value) > 0 :
                    
                    value = value[0]  
                
                else:

                    select = driver.find_elements(By.XPATH,"//*[@id='"+tablename+"']/tbody/tr["+str(x)+"]/td["+str(y)+"]/select")
                    value = [Select(elm).first_selected_option.text for elm in select]
                    
                    if len(value) > 0:
                        value= value[0]
                    else:
                        value = ""


            if celltype == 1:
                title = [elm.get_attribute("innerText") for elm in cell]
                title = title[0].replace(" ","_")
                title = title.replace("(","")
                title = title.replace(")","")

            data[title]  = value
    return data
