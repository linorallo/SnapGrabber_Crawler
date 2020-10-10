from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium import webdriver
import time 
import persistance
  
# Replace below path with the absolute path 
# to chromedriver in your computer 

def open_browser():
    return webdriver.Chrome()


def get_contacts():
    driver = open_browser()
    driver.get('https://chrome.google.com/webstore/detail/snapaddy-grabber/pijkopmmbakjnkbhlhmoiakmdjomjppo')
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div').click()
    time.sleep(10)
    for url in readURL():
        driver.get(url) 
        WebDriverWait(driver, 600)
        information = driver.find_element_by_class('caja_contenido_ficha').text[0]
        print(information)
        driver.get('chrome-extension://pijkopmmbakjnkbhlhmoiakmdjomjppo/popup_dist/index.html#/grabber/list')
        create_contact = driver.find_element_by_class('qa-paste-contact-data animated')
        create_contact.send_keys(information)
        WebDriverWait(driver, 600)


        


def showContacts():
    contacts = getContacts()
    print(contacts)
    return contacts



