"""
This module contains menu to GUI
 for transfering files from JT fo the Process Simulate project folder. 
Actual Tasks:
1. Define a method to populate Mapping Library
2. Find a way to compile documentation intellegently. 
3. In a Map file could be duplicates
4.  
"""
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from shutil import copyfile
from re import *
import Dictionary
import os
import shutil
class GUI:
    
    entry=" "
    projectPath="new path"    
    listOfFileNames=[]
    transformDict = {}
    unresolvedDict={}
    window = Tk()

    def __init__(self):
        pass
    def openFiles(self):    
        """
    Open files and identify whether the files are presented in the Tecnomatix Library.  
        """
        filez = filedialog.askopenfilenames(parent=self.window,title='Choose a file')
        listOfFileNames=list(filez)
        self.parseEntry(listOfFileNames)
    
    def browseFolder(self):    
        self.projectPath= filedialog.askdirectory()  
        
    def parseEntry(self,fileList):  
        """
    Parses file names. Creates Dictionary of files to be transfered to Tecnomatix format 
    and dictionary of unparsed entries.    
        """
        entryType=""
        dictionary=Dictionary.readFromFile()
        self.transformDict = {}
        self.unresolvedDict={}    
        for entry in fileList:  
            path=entry
            fileName=entry.split('/')[-1]
            flag=False
            for key,val in dictionary.items():
                for pattern in val:                
                    match = re.search(pattern, fileName,flags=re.IGNORECASE)
                    if match:                    
                       # print("match")
                        flag=True
                        self.transformDict[path]=key                    
                        break
                if flag:                
                    break        
            if not flag:
                self.unresolvedDict[path]= fileName
        if self.unresolvedDict.len!=0:
            self.defineMapping()
                
    
    def transferFiles(self):            
            
        for key, val in self.transformDict.items():            
            source=key.encode('unicode-escape')
            destination=self.projectPath.encode('unicode-escape')           
            shutil.copy(source , destination)            
            print (key + " is " + val)       
       
        
    def defineMapping(self):
        print("DefineMapping")
        pass
        
    
    def clearUnresolvedFiles(self):
        self.unresolvedDict={}        
   
gui = GUI() 
gui.window.title("Process Simulate Transformer")
#gui.window.geometry('500x400')
gui.lbl = Label(gui.window, text="Please select JT files to be transformed")
gui.lbl.grid(column=0, row=0, pady=20)

selectFiles = Button(gui.window, text="Select Files", command=gui.openFiles)
selectDirectory = Button(gui.window, text="Choose directory", command=gui.browseFolder)
performTransformation= Button(gui.window, text="Transform", command=gui.transferFiles)
selectFiles.grid(column=0, row=1,sticky=W, pady=5, padx=10)
selectDirectory.grid(column=0, row=2,sticky=W, pady=5, padx=10)
performTransformation.grid(column=0, row=3,sticky=W, pady=5, padx=10)
mappingEntry = Entry()

mappingEntry.grid(column=2, row=1, sticky=W, pady=0, padx=10)

print(gui.projectPath)

gui.window.mainloop()


        


