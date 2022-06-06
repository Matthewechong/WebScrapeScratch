from selenium import webdriver
from selenium.webdriver.common.by import By
PATH = 'WebScraping_Scratch/chromedriver'
driver = webdriver.Chrome(PATH)
URL = 'https://www.smogon.com/dex/ss/formats/ou/'
driver.get(URL)
data = driver.find_element(By.CLASS_NAME, value='theme--dark')
data = data.find_element(By.ID, value='container')
data = data.find_element(By.CLASS_NAME, value='DexBody')
data = data.find_element(By.CLASS_NAME, value='DexContent')
data = data.find_elements(By.TAG_NAME, value='section')
pokemons = data[2].find_elements(By.CLASS_NAME, value='PokemonAltRow')
for pokemon in pokemons:
    print(pokemon.text + '\n')
driver.quit()
