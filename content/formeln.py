from fnmatch import fnmatch
import os
wd = os.path.dirname(os.path.realpath(__file__))
dir = input("Verzeichnis: ")
pattern = "*.md"

paths = []

for path, subdirs, files in os.walk(os.path.join(wd,dir)):
	for name in files:
		if fnmatch(name, pattern):
			paths.append(os.path.join(path, name))
paths.sort(key = lambda x: x.split("/")[-1])
callouts = {}
for path in paths:
	with open(path,"r") as file:
		lines = file.readlines()
		callout = ""
		callouts_in_file = []
		for line in lines:
			if line.startswith(">"):
				callout = callout + line
			elif  callout:
				callouts_in_file.append(callout)
				callout = ""
		if callouts_in_file:
			callouts[os.path.basename(path)]=callouts_in_file

with open(os.path.join(wd,dir,"Formeln.md"),"w") as file:
    for k in list(callouts.keys()):
     file.write(f"# {k[:-3]}\n")
     for c in callouts[k]:
        file.write(c)
        if c.startswith(">[!"):
            file.write("\n")



     
