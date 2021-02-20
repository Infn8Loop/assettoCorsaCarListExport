# This version only exports the name, brand, and class into your file. 


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

wrFile = open("carList.csv", 'w')

wrFile.write("")
wrFile.close()
wrFile = open("carList.csv", 'a')


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
