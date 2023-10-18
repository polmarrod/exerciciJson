from globales import constants, getChars
from character import Character
from character_films import Character_films
import json

def main ():
    character_film_list = getChars()
    for char in character_film_list:
        char.info
    character : Character_films = any("Luke Skywalker" in chars.__name for chars in character_film_list)
    character.info
    #f_new= open("Characters.json", 'w')
    #json.dump(char.__dict__, f_new, indent = 4)

main()
