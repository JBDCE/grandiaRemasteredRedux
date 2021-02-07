'''
Script to find patterns by dumping their hex values and searching for the pattern.
All this could most likely be done with regex but i am a scrub in python
and even worse in regex so im trying this aproach
'''
import os

folderToBeSearched = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\GRANDIA HD Remaster\\content" # TODO Make this a command line arg
patternList = [] # TODO Make this a command line arg
minFound  = 0 # TODO command line arg

fileList = [] # Create a list of all files in the folder and its subfolders
for root, dirs, files in os.walk(folderToBeSearched):
	for file in files:
		fileList.append(os.path.join(root,file))


for file in fileList:
    # Open the file in binary and dump its hex value
    with open(file, 'rb') as bin:
        foundCounter = 0
        for pattern in patternList:
            # Search for the patterns one after the other
            # TODO Have an argument to mind the order of the patterns
            if pattern in bin:
                # Count the number of patterns that matched in every file
                foundCounter += 1
    # If more than number of patterns were found print its filepath and the number of matches
    # TODO Have an argument to make this unix clean
    if foundCounter < minFound:
        print(str(file) + "Matches: " + foundCounter + "args")


