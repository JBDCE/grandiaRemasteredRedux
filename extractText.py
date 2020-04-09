'''
This file is running the subroutine to generating 
the Text files needed for the Modded Dialog and 
Hint messages found at the save point around the game
'''


import os

def getStartPattern(fileObject):
    fileObject.seek(0, 0)
    return fileObject.read(PATTERN_LENGHT)


def getEndPattern(fileObject):
    fileObject.seek(-PATTERN_LENGHT, 2)
    return fileObject.read(PATTERN_LENGHT)


def createFileList(diffFilePath):
    preparedInput = []
    with open(diffFilepath, 'r') as diffFile:
        rawInput = diffFile.readlines()
        for line in rawInput:
            if os.path.splitext(line[:-1])[1] == ".MDP":
                preparedInput.append("FIELD/" + line[:-5])

    return preparedInput


REMASTER_CONTENT_PATH = "TestFileStructure/RemasterGameFiles/content/"
REDUX_BIN_EXTRACT_PATH = "TestFileStructure/ReduxGameFiles/"
PATTERN_LENGHT = 7
OUTPUT_PATH = "TestFileStructure/Output/"
# SOURCE_PATH = "Experiment Files/Remaster/"  # "Experiment Files/ReduxFiles/"
# DEST_PATH = ""

# Create File list from diff file
diffFilepath = "ReduxFileList.txt"
fileList = createFileList(diffFilepath)


for filePath in fileList:
    # Open the original Files to Determine a pattern
    # for start and finish of the text documents
    startPattern = None
    endPattern = None
    preparedPath = REMASTER_CONTENT_PATH + "TEXT/EN/" + os.path.split(filePath)[1] + ".SCN"

    if not os.path.isfile(preparedPath):
        print(filePath + "does not contain text")
        continue

    with open(preparedPath, 'rb') as fileObject:
        startPattern = getStartPattern(fileObject)
        endPattern = getEndPattern(fileObject)

    # Read Redux patched Files and Search for start and end Pattern
    textContent = None
    with open(REDUX_BIN_EXTRACT_PATH + filePath + ".MDP", 'rb') as fileObject:
        fileContent = fileObject.read()
        startLocation = fileContent.find(startPattern)
        endLocation = fileContent.find(endPattern)

        textLength = endLocation - startLocation + PATTERN_LENGHT
        fileObject.seek(startLocation, 0)
        textContent = fileObject.read(textLength)

    # Write the extract to an output file
    target = OUTPUT_PATH + filePath + ".SCN"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, 'wb+') as outputFile:
        outputFile.write(textContent)

# lines = []
# with open(SOURCE_PATH + "2C00.SCN", 'rb') as f:
#     lines = f.readlines()
#     print(lines)
