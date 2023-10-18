import json
from character import Character

class constants ():
    PATHFITXEROJSON = "json/StarWars.json"

def getChars():
    try:
        with open(constants.PATHFITXEROJSON, 'r') as fileReader:
            data = json.load(fileReader)
        characters = []
        characters = [Character(**item["fields"]) for item in data]
        return characters
    except :
        print ("Hi ha Hagut un error")
        return None