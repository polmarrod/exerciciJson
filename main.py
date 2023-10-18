from globales import constants, getChars
from character import Character
from character_films import Character_films
import json

def main ():
    character_film_list = getChars()
    for index, char in enumerate(character_film_list):
        char.info
        if char.getName == "Luke Skywalker":
            
        if char.getName == "":


    #f_new= open("Characters.json", 'w')
    #json.dump(char.__dict__, f_new, indent = 4)

main()
