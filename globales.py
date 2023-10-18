import json
from character import Character
from character_films import Character_films

class constants ():
    PATHFITXEROJSON = "json/StarWars.json"

def getChars():
    try:
        with open(constants.PATHFITXEROJSON, 'r') as fileReader:
            data = json.load(fileReader)
        character_film_list = []
        character_film_list = [Character_films(**item["fields"]) for item in data]
        return character_film_list
    except :
        print ("Hi ha Hagut un error")
        return None