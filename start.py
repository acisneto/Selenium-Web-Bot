import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytesseract

driver = webdriver. Firefox()
connectButton = driver.find_element(By.ID, "connectButton") 
actionchains = ActionChains(driver)
ActionChains(driver).click(connectButton).perform()
time.sleep(5)
driver.get("https://accounts.google.com")
time.sleep(7)


select LogIn = driver.find_element(By.XPATH, "//input[@id='identifierId']") ActionChains (driver).click(selectLogin).perform()
LogIn = driver.find_element(By.ID, "identifierId")
LogIn.send_keys("teste")
LogIn.send_keys(Keys.ENTER)
time.sleep(5)
selectCaptcha driver.find_element(By.CLASS_NAME, "TrZEUC")
captchaimg = selectCaptcha.screenshot("teste.png")
time.sleep(3)
captchatext = pytesseract.image_to_string(captchaimg)
print(captchatext)
