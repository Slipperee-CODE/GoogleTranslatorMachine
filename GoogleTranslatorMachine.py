from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
options.add_argument('--headless')
options.add_argument('--log-level=3')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://translate.google.com/")

def click_element(element):
    button = driver.find_element(By.XPATH, element)
    driver.execute_script("arguments[0].click();", button)

def send_text(element, text):
    textBox = driver.find_element(By.XPATH, element)
    textBox.send_keys(text)


def clear_text(element):
    textBox = driver.find_element(By.XPATH, element)
    textBox.clear()

    
#send_text('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea', "Hello World")
click_element('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/button/div[3]')


allLanguages = driver.find_element("xpath", '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div')

allLanguages = allLanguages.find_elements(By.CLASS_NAME, "qSb8Pe")

languageSelectList = [language.text for language in allLanguages]




while True:
    languageInput = input("Enter the language you want to translate to: ")

    languageInput = languageInput[0].upper() + languageInput[1:].lower()

    if languageInput in languageSelectList:
        print("Language found!")
        index = languageSelectList.index(languageInput)
        languageToUse = allLanguages[index]
        driver.execute_script("arguments[0].click();", languageToUse)
        break
    else:
        print("Language not found!")

    
click_element('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[3]/div/span/button/div[3]')

wordsToTranslate = input("Enter the words you want to translate: ")
send_text('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea', wordsToTranslate)
timestoTranslate = int(input("How many times do you want to translate it? "))


time.sleep(0.1)


for i in range(timestoTranslate):
    click_element('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[3]/div/span/button/div[3]')
    time.sleep(0.1)

print("Done!")

time.sleep(0.5)

resultBox = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]')

print("Translated text: " + resultBox.text)


driver.close()
driver.quit()