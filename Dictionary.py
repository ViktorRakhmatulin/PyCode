"""
This module contains methods to deal with the dictionary aimed to collect names of objects 
in Tecnomatix and  corresponding pattern in name. 
"""

import json
objectDict = {}

def addValue(key,value):
    objectDict[key]=value

def deleteValue(mapFile,key):
    mapFile.pop(key)
     
def getDictionary():
    
    return objectDict

def writeToFile(mapFile):    
    file=open("items2.json","w")
    jsonFile=json.dumps(mapFile)
    file.write(jsonFile)
    file.close()
def readFromFile():
    """
Reads a data from file written in json format and returns the dictionary.
    """
    file=open("items2.json","r")    
    jsonFile=file.read()
    mapFile=json.loads(jsonFile)
    file.close()
    print(mapFile)
    return mapFile
    
#myMapFile=readFromFile()
#myMapFile.pop("conveyor")
#print(myMapFile)

#addValue("conveyor",["cnv","con","cnn"])
#addValue("conveyor2",["cnv1","con2","cnn3"])
#writeToFile(objectDict)
    
    
#
#print(tel==tel2)
#tel2["device"]= [500,2,6]
#print (tel2)

##xml = dicttoxml.dicttoxml(tel)
#dom = parseString(xml)
#resultedXML=dom.toprettyxml()

#


