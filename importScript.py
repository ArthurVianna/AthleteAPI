import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AthleteAPI.settings")
django.setup()

from Athlete.importAthleteCSV import *

if len(sys.argv) >= 3:
    pathNOC = sys.argv[1]
    pathAthlete = sys.argv[2]
    if validateNOCCSV(pathNOC):
        thread = threading.Thread(target=importNOCCSV, args=(pathNOC))
        thread.daemon = True
        thread.start()
        pass

    if validateAthleteCSV(pathAthlete):
        thread = threading.Thread(target=importAthleteCSV, args=(pathAthlete))
        thread.daemon = True
        thread.start()
        pass