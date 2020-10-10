from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium import webdriver
import time 
import persistance
  
# Replace below path with the absolute path 
# to chromedriver in your computer 


def get_contacts():
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=/home/lino/snap/chromium/common/chromium/Profile 1')
    driver = webdriver.Chrome(executable_path='/snap/chromium/1328/usr/lib/chromium-browser/chrome', chrome_options=options)
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



