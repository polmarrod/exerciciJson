from globales import constants, getChars
from character import Character
import json

def main ():
    characters = getChars()
    for char in characters:
        char.info
    #f_new= open("Characters.json", 'w')
    #json.dump(char.__dict__, f_new, indent = 4)

main()

