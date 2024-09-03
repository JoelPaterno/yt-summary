from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/watch?v=NB8OceGZGjA")

time.sleep(5)

input_element = driver.find_element(By.CLASS_NAME, "style-scope ytd-video-description-transcript-section-renderer")   
input_element.click()

driver.quit()