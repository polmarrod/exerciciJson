from globales import constants, getFile
from character import Character

def main ():

    char = Character(
        edited= "2014-12-20T21:17:56.891Z",
        name= "Luke Skywalker",
        created= "2014-12-09T13:50:51.644Z",
        gender= "male",
        skin_color= "fair",
        hair_color= "blond",
        height= "172",
        eye_color= "blue",
        mass= "77",
        homeworld= 1,
        birth_year= "19BBY")
    char.info

main()

