from globales import constants, getChars
from character import Character
from character_films import Character_films
import json

def main ():
    character_film_list = getChars()
    for index, char in enumerate(character_film_list):
        if char.getName == "Anakin Skywalker":
            character_film_list[index].alive_at_the_end = "NO"
            character_film_list[index].first_film = "STAR WARS I"
            character_film_list[index].num_of_films = "6"
        if char.getName == "Luke Skywalker":
            character_film_list[index].alive_at_the_end = "SI"
            character_film_list[index].first_film = "STAR WARS IV"
            character_film_list[index].num_of_films = "6"
        if char.getName == "Luke Skywalker":
            character_film_list[index].alive_at_the_end = "SI"
            character_film_list[index].first_film = "STAR WARS IV"
            character_film_list[index].num_of_films = "7"
        char.info
    newFile = open("json/Characters.json", 'w')
    jsonString = json.dumps([char.__dict__ for char in character_film_list], indent = 4)
    print(jsonString)
    newFile.write(jsonString)
main()
