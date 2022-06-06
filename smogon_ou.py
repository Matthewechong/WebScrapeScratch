from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

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

new_columns = {'PokemonAltRow-name': 'Name',
               'PokemonAltRow-types': 'Type',
               'PokemonAltRow-abilities': 'Abilities',
               'PokemonAltRow-tags': 'Tier',
               'PokemonAltRow-hp': 'Hp',
               'PokemonAltRow-atk': 'Atk',
               'PokemonAltRow-def': 'Def',
               'PokemonAltRow-spa': 'Spa',
               'PokemonAltRow-spd': 'Spd',
               'PokemonAltRow-spe': 'Spe'}
stats = ['Hp', 'Atk', 'Def', 'Spa', 'Spd', 'Spe']


PATH = '/Users/chongster/Desktop/Code/Python/WebScraping_Scratch/chromedriver'


def get_data():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)

    data = driver.find_element(By.CLASS_NAME, value='theme--dark')
    data = data.find_element(By.ID, value='container')
    data = data.find_element(By.CLASS_NAME, value='DexBody')
    data = data.find_element(By.CLASS_NAME, value='DexContent')
    data = data.find_elements(By.TAG_NAME, value='section')
    pokemons = data[2].find_elements(By.CLASS_NAME, value='PokemonAltRow')
    all_data = []
    for pokemon in pokemons:
        temp = {}
        for atrribute in attributes:
            value = pokemon.find_element(By.CLASS_NAME, value=atrribute).text
            temp[atrribute] = value
        all_data.append(temp)

    driver.quit()
    return all_data


def clean_stats(stat):
    data = stat.split('\n')
    return data[len(data)-1]


def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    clean_df = df.rename(columns=new_columns)
    for stat in stats:
        clean_df[stat] = clean_df[stat].apply(clean_stats)
    return clean_df
