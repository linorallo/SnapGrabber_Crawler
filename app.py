from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium import webdriver
import selenium
import time 
import persistance
import pyperclip
import phone_extractor
from urlextract import URLExtract

  
# Replace below path with the absolute path 
# to chromedriver in your computer 

def paste_keys(self, xpath, text):
    os.system("echo %s| clip" % text.strip())
    el = self.driver.find_element_by_xpath(xpath)
    el.send_keys(Keys.CONTROL, 'v')

def get_contacts():
    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir=C:\\Users\\Lino Rallo\\AppData\\Local\\Google\\Chrome\\User Data')
    option.add_argument('--profile-directory=Default')
    driverpath = 'C:\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driverpath, options= option)

    #option = webdriver.EdgeOptions()
    #option.use_chromium() = True
    #option.add_argument('--user-data-dir=C:\\Users\\Lino Rallo\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 1')
    #option.add_argument('profile-directory=Profile 1')
    #driverpath = "C:\\Users\\Lino Rallo\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe" 
    #driver = webdriver.Edge(driverpath,options=option)
    
    #driver = webdriver.Chrome(executable_path='/snap/chromium/1328/usr/lib/chromium-browser/chrome', chrome_options=options)
    
    for url in persistance.readURL():
        try:
            driver.get(url) 
            time.sleep(3)
            information=''
            information = driver.find_element_by_class_name('caja_contenido_ficha').text
            pyperclip.copy(information)
            print(information)
            phones = phone_extractor.PhoneNumberExtractor().extract_phone_numbers(information)
            if  len(str(phones))>2 or len(str(URLExtract().find_urls(information)))>5 :
                driver.get('chrome-extension://pijkopmmbakjnkbhlhmoiakmdjomjppo/popup_dist/index.html#/grabber/list')
                create_contact = driver.find_element_by_xpath('/html/body/snapaddy-grabber/div[1]/grabber-list/main/div/grabber-list-copy-paste-bar/div/div[3]/div/grabber-list-paste-box/textarea')
                create_contact.send_keys(Keys.CONTROL, 'v')
                time.sleep(3)
        except selenium.common.exceptions.NoSuchElementException as err:
            print(err)
            print('Skipped: '+url)

get_contacts()
        


def showContacts():
    contacts = getContacts()
    print(contacts)
    return contacts



