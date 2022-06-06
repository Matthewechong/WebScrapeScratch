from selenium import webdriver
from selenium.webdriver.common.by import By


# URL to look up website
URL = 'https://www.smogon.com/dex/ss/formats/ou/'
# Information to scrape
attributes = ['PokemonAltRow-name',
              'PokemonAltRow-types',
              'PokemonAltRow-abilities',
              'PokemonAltRow-tags',
              'PokemonAltRow-hp',
              'PokemonAltRow-atk',
              'PokemonAltRow-def',
              'PokemonAltRow-spa',
              'PokemonAltRow-spd',
              'PokemonAltRow-spe']


PATH = '/Users/chongster/Desktop/Code/Python/WebScraping_Scratch/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get(URL)

data = driver.find_element(By.CLASS_NAME, value='theme--dark')
data = data.find_element(By.ID, value='container')
data = data.find_element(By.CLASS_NAME, value='DexBody')
data = data.find_element(By.CLASS_NAME, value='DexContent')
data = data.find_elements(By.TAG_NAME, value='section')
pokemons = data[2].find_elements(By.CLASS_NAME, value='PokemonAltRow')
for pokemon in pokemons:
    temp = {}
    for atrribute in attributes:
        value = pokemon.find_element(By.CLASS_NAME, value=atrribute).text
        temp[atrribute] = value
    print(temp)

driver.quit()
