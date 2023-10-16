import json
from character import Character

class constants ():
    PATHFITXEROJSON = "json/StarWars.json"

def toClass():
    
    return 

def getFile():
    path = constants.PATHFITXEROJSON
    try:
        with open('tu_archivo.json', 'r') as fileReader:
            data = json.load(fileReader)
        characters = [Character(**item) for item in data]
        return characters
    except:
        print ("Hi ha Hagut un error")
        return None