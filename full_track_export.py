import json
import os
import glob

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

dirlist = glob.glob("./tracks/*")

wrFile = open("trackList.csv", 'w')

wrFile.write("")
wrFile.close()
wrFile = open("trackList.csv", 'a')


for dir in dirlist:
    filepath = str(dir) + "/ui/ui_track.json"
    if os.path.exists(filepath):
        addString = ""
        fileread = open(filepath, 'rb')
        jsonstr = fileread.read()
        # print(jsonstr)
        if validateJSON(jsonstr):
            print(filepath + " is valid")
            carobj = json.loads(jsonstr)
            # keyList = ["name", "brand", "class"]
            keyList = carobj.keys()
            for key in keyList:
                if key in carobj.keys():
                    addString += (str(carobj[key]).replace(",", "") + ",").encode("ascii", 'ignore').decode('ascii', 'ignore').strip()
            wrFile.write(str(addString) + "," + str(filepath))
            wrFile.write("\n")
        else:
            print(filepath + " is invalid")
        fileread.close()
