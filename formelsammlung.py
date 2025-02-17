#!/usr/bin/env python3
import os
from os import walk
import re
from os.path import isfile, join

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text)]


p = join(os.getcwd(),"content","AC","Klausur (oh je)")
fs = []
for path, subdirs, files in os.walk(p):
    for name in files:
        fs.append(os.path.join(os.getcwd(),"content","AC","Klausur (oh je)",path, name))

print(files)
fs.sort(key=natural_keys)
print(fs)
formelsammlung = open(join(os.getcwd(),"content","AC","Klausur (oh je)","Formelsammlung.md"),"w")    
formelsammlung.close()

fs.remove((os.path.join(os.getcwd(),"content","AC","Klausur (oh je)","Formelsammlung.md")))

for file in fs:
    formelsammlung = open(join(os.getcwd(),"content","AC","Klausur (oh je)","Formelsammlung.md"),"a")    
    formelsammlung.write("# " + os.path.basename(file).replace(".md","")+"\n")
    note = open(file,"r").readlines()
    
    c_string = ""
    callout = False
    callouts = []
    
    for line in note:
        if line.startswith(">[!important]"):
            callout = True
         
        if(callout and  not line.startswith(">")):
            callouts.append(c_string)
            callout = False
            c_string = ""
            
        if (callout):
            c_string+=  (line)
    
    if (c_string != ""):
        callouts.append(c_string)
        callout = False
        c_string = ""
        
    for c in callouts:
        formelsammlung.write(c +"\n")
        
    callouts = []    
    
    
