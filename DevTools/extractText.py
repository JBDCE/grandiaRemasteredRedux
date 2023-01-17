'''
This file is running the subroutine to generating
the Text files needed for the Modded Dialog and
Hint messages found at the save point around the game
'''


import os


def getStartPattern(fileObject):
    fileObject.seek(0, 0)
    return fileObject.read(START_PATTERN_LENGHT)


def getEndPattern(fileObject):
    fileObject.seek(-END_PATTERN_LENGHT, 2)
    return fileObject.read(END_PATTERN_LENGHT)


def createFileList(diffFilePath):
    preparedInput = []
    with open(diffFilepath, 'r') as diffFile:
        rawInput = diffFile.readlines()
        for line in rawInput:
            if os.path.splitext(line[:-1])[1] == ".MDP":
                preparedInput.append(line[:-5])

    return preparedInput


REMASTER_CONTENT_PATH = "TestFileStructure/RemasterGameFiles/"
REDUX_BIN_EXTRACT_PATH = "TestFileStructure/ReduxGameFiles/"
START_PATTERN_LENGHT = 8
END_PATTERN_LENGHT = 15
OUTPUT_PATH = "TestFileStructure/Output/"
# SOURCE_PATH = "Experiment Files/Remaster/"  # "Experiment Files/ReduxFiles/"
# DEST_PATH = ""

# Create File list from diff file
diffFilepath = "FieldDiffFile.txt"
fileList = createFileList(diffFilepath)


for filePath in fileList:
    # Open the original Files to Determine a pattern
    # for start and finish of the text documents
    startPattern = None
    endPattern = None
    preparedPath = REMASTER_CONTENT_PATH + "TEXT/EN/" + os.path.split(filePath)[1] + ".SCN"
    originalSize = os.path.getsize(preparedPath)

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
        endLocation = fileContent.rfind(endPattern)

        assert startLocation != -1,\
            "Start pattern was not found in file: " + filePath
        assert endLocation != -1,\
            "End pattern was not found in file: " + filePath

        textLength = endLocation - startLocation + END_PATTERN_LENGHT
        fileObject.seek(startLocation, 0)
        textContent = fileObject.read(textLength)

    # Write the extract to an output file
    target = OUTPUT_PATH + filePath + ".SCN"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, 'wb+') as outputFile:
        outputFile.write(textContent)

    # assert os.path.getsize(target) == originalSize,\
        "Sizes dont match"

# lines = []
# with open(SOURCE_PATH + "2C00.SCN", 'rb') as f:
#     lines = f.readlines()
#     print(lines)

# Apparently the output causes issues with the map 4c0c Manual edit at output required should be included in Release 0.4.2
