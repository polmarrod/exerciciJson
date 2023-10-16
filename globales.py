import csv
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = None
    while file_path == None:
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("CSV Files", "*.csv"), ("All files", "*.*")])
        if file_path != None:
            return file_path
class constants ():
    PATHNEWFITXERO = "jugadors_basket.csv"
    PATHFITXEROJSON = "jugadors_basket.json"
    FOOT = 2.54
    POUND = 0.45
    SEPARADOROLD= ";"
    SEPARADORNEW = "^"
    NAME = "names"
    TEAM = "team"
    POSITION = "position"
    HEIGHT = "height"
    WEIGHT = "weight"
    AGE = "age"
    NEWHEADERS = ["Nom", "Equip", "Posicio", "Altura", "Pes", "Edat"]
    NEWPOSITIONS = {
        "Point Guard" : "Base",
        "Shooting Guard" : "Escorta",
        "Small Forward" : "Aler",
        "Power Forward" : "Ala-pivot",
        "Center" : "Pivot"
    }

def toDictionarie(reader : enumerate):
    dictionarie = {
        constants.NAME : [],
        constants.TEAM : [],
        constants.POSITION : [],
        constants.HEIGHT : [],
        constants.WEIGHT : [],
        constants.AGE : []
    }
    for index, row in reader:
        if index != 0:
            dictionarie[constants.NAME].append(row[0])     
            dictionarie[constants.TEAM].append(row[1])  
            dictionarie[constants.POSITION].append(row[2])     
            dictionarie[constants.HEIGHT].append(row[3])  
            dictionarie[constants.WEIGHT].append(row[4])  
            dictionarie[constants.AGE].append(row[5])  
    return dictionarie

def showLines(reader : enumerate):
    for index, row in reader:
        print(",".join(row) , end=" ")
        print("Row number:" + str(index))

def showParameter (book : dict[str, list], parameter: str):
    for thing in book[parameter]:
        print(thing)

def getFile(separador: str):
    path = getPath()
    try:
        fileReader = open(path, "r", encoding= "ASCII")
        filecsv = csv.reader(fileReader,  delimiter = separador,)
        return enumerate(filecsv)
    except:
        print ("Hi ha Hagut un error")
        return None

def toListOfDictionaries(reader : enumerate):
    listDict = []
    for index, row in reader:
        if index != 0:
            listDict.append(
                {
                    constants.NAME : row[0],
                    constants.TEAM : row[1],
                    constants.POSITION : row[2],
                    constants.HEIGHT : float(row[3]),
                    constants.WEIGHT : float(row[4]),
                    constants.AGE : float(row[5])
                }
            )
    return listDict
def getPath():
    filename = open_file_dialog()

    return filename
