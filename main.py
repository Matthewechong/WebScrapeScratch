import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Access to enter key, search key
from selenium.webdriver.common.keys import Keys

PATH = 'WebScraping_Scratch/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://www.techwithtim.net')
title = driver.title

search = driver.find_element(by=By.NAME, value="s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_element("article")
    for article in articles:
        header = article.find_element("entry-summary")
        print(header.text + '\n')
finally:
    driver.quit()
