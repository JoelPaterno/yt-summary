from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

def scrape_website(website) -> None:
    print("launching chrome browser...")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(website)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'expand'))
        )
        element.click()
        element2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.yt-spec-button-shape-next'))
        )
        print("button found...")
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView();", element2)
        time.sleep(5)
        element2.click()
        time.sleep(5)
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    return cleaned_content