import csv
from Athlete.models import *

def readFileAsDict(path):
    return csv.DictReader(open(path))

def importNOCCSV(path):
    openedCSV = readFileAsDict(path)

    for row in openedCSV:
        noc = row["NOC"]
        nocObj,created = NOC.objects.get_or_create(noc=noc)
        nocObj.region = row["region"]
        nocObj.notes = row["notes"]

        nocObj.save()

def validateNOCCSV(path):
    needed_data = ["NOC", "region", "notes"]
    return validateCSV(path,needed_data)

def validateAthleteCSV(path):
    needed_data = ["NOC", "Name", "Sex","Height","Weight","Games","Year","Season","City","Sport","Event","Medal","Age","Team"]
    return validateCSV(path,needed_data)
    

def validateCSV(path,needed_data):
    if not path.endswith(".csv"):
        return False
    columns = set()
    with open(path, 'rt') as fin:
        csvin = csv.reader(fin)
        columns.update(next(csvin, []))
    fin.close()
    return all(elem in columns for elem in needed_data)

def importAthleteCSV(path):
    openedCSV = readFileAsDict(path)
    
    for row in openedCSV:
        
        athlete = athleteImport(row)
        olympic = olympicsImport(row)
        event = eventImport(row)
        city,created =  City.objects.get_or_create(name=row["City"])

        """for key,value in row.items():
            if key in columnKeys.keys():
                kwargs[columnKeys[key]] = value"""
        kwargs = {}
        kwargs["athlete"] = athlete
        kwargs["olympic"] = olympic
        kwargs["city"] = city
        kwargs["event"] = event
        kwargs["age"] = parseToIntOrNone(row["Age"])
        if(row["Medal"] != "NA"):
            kwargs["medal"] = row["Medal"]
        else:
            kwargs["medal__isnull"] = True
        kwargs["team"] = row["Team"]


        Participation.objects.get_or_create(**kwargs)


    
        

def athleteImport(rowDict):
    args = {}
    args["name"] = rowDict["Name"]
    args["sex"] = rowDict["Sex"]
    args["height"] = parseToIntOrNone(rowDict["Height"])
    args["weight"] = parseToIntOrNone(rowDict["Weight"])
    args["noc"],created = NOC.objects.get_or_create(noc=rowDict["NOC"])

    athlete,created = Athlete.objects.get_or_create(**args)
    return athlete

def olympicsImport(rowDict):
    args = {}
    
    args["name"] = rowDict["Games"]
    args["year"] = parseToIntOrNone(rowDict["Year"])
    args["Season"] = rowDict["Season"]

    olymp,created = Olympics.objects.get_or_create(**args)
    return olymp

def eventImport(rowDict):
    args = {}
    
    args["sport"],created = Sport.objects.get_or_create(name=rowDict["Sport"])
    args["name"] = rowDict["Event"]

    event,created = Event.objects.get_or_create(**args)
    return event

def parseToIntOrNone(str):
    try:
        return int(str)
    except ValueError:
        return None


