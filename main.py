from globales import constants, getChars
from character import Character

def main ():
    characters = getChars()
    for char in characters:
        char.info

main()

