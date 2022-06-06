from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.smogon.com/dex/ss/pokemon/dragonite/'
PATH = '/Users/chongster/Desktop/Code/Python/WebScraping_Scratch/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get(URL)
data = driver.find_element(By.CLASS_NAME, value="theme--dark")
data = data.find_element(By.ID, value='container')
data = data.find_element(By.CLASS_NAME, value='DexBody')
data = data.find_element(By.CLASS_NAME, value='DexContent')
data = data.find_elements(By.TAG_NAME, value='section')
data = data[2]
data = data.find_elements(By.CLASS_NAME, value='BlockMovesetInfo')
all_data = []
for d in data:
    all_data.append(d.text)
print(all_data)
driver.close()
