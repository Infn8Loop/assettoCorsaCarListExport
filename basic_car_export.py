# This version only exports the name, brand, and class into your file. 
# Pop this file into your Assetto Corsa 'content' folder. 
# enter a command prompt in the same folder
# run 'python export_car_list.py' 
# the CSV file outputs to the same directory - just import it into your favorite spreadsheet software

import json
import os
import glob

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

dirlist = glob.glob("./cars/*")

wrFile = open("basicCarList.csv", 'w')

wrFile.write("name,brand,class\n")
wrFile.close()
wrFile = open("basicCarList.csv", 'a')


for dir in dirlist:
    filepath = str(dir) + "/ui/ui_car.json"
    if os.path.exists(filepath):
        addString = ""
        fileread = open(filepath, 'rb')
        jsonstr = fileread.read()
        # print(jsonstr)
        if validateJSON(jsonstr):
            print(filepath + " is valid")
            carobj = json.loads(jsonstr)
            keyList = ["name", "brand", "class"]
            # keyList = carobj.keys()
            for key in keyList:
                if key in carobj.keys():
                    addString += (str(carobj[key]) + ",").encode("ascii", 'ignore').decode('ascii', 'ignore').strip()
            wrFile.write(str(addString) + "," + str(filepath))
            wrFile.write("\n")
        else:
            print(filepath + " is invalid")
        fileread.close()
