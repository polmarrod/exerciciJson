        
class constants ():
    PATHFITXEROJSON = "jugadors_basket.json"

def toClass(reader : enumerate):
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

def getFile(separador: str):
    path = constants.PATHFITXEROJSON
    try:
        fileReader = open(path, "r", encoding= "ASCII")
        'filecsv = csv.reader(fileReader,  delimiter = separador,)'
        return enumerate(filecsv)
    except:
        print ("Hi ha Hagut un error")
        return None