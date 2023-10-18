from globales import constants, getChars
from character import Character
import json

def main ():
    characters = getChars()
    for char in characters:
        char.info

    f_json = open("./json/StarWars.json")
    data = json.load(f_json)
    chars_list = []

    for item in data:
        char = Character(**item["fields"])
        char.info
        chars_list.append(char)

    #f_new= open("Characters.json", 'w')
    #json.dump(char.__dict__, f_new, indent = 4)

main()

