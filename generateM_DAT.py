REMASTER_MDAT = open("TestFileStructure/original_M_DAT.BIN", 'rb')
REDUX1_MDAT = open("TestFileStructure/redux1_M_DAT.BIN", 'rb')
REDUX2_MDAT = open("TestFileStructure/redux2_M_DAT.BIN", 'rb')
NAMES_TXT = open("TestFileStructure/names.txt", 'r')

redux1Bytes = []
redux2Bytes = []
remasterBytes = []

protectedBytes = []

allowedChars = [32]
for i in range(65, 91):
    allowedChars.append(i)
for i in range(97, 123):
    allowedChars.append(i)


def populateByteLists():
    global redux1Bytes, redux2Bytes, remasterBytes, protectedBytes

    rawBytes = REMASTER_MDAT.read()
    names = NAMES_TXT.readlines()

    for name in names:
        name = name.rstrip()
        byteName = bytes(name, encoding='ascii')
        startAddress = rawBytes.find(byteName)

        if startAddress == -1:
            print(name + " not found in M_DAT")
        else:
            protectedBytes += list(range(startAddress, startAddress+len(name)))

    remasterBytes = bytearray(rawBytes)

    # the three files should all be equal in l ength
    rawBytes = REDUX1_MDAT.read()
    redux1Bytes = bytearray(rawBytes)
    assert len(redux1Bytes) == len(remasterBytes),\
        "Redux1_MDAT is the wrong length"

    rawBytes = REDUX2_MDAT.read()
    redux2Bytes = bytearray(rawBytes)
    assert len(redux2Bytes) == len(remasterBytes),\
        "Redux2_MDAT is the wrong length"

    print("Remaster lenght: " + str(len(remasterBytes)))


def performChanges():
    global remasterBytes, redux1Bytes, redux2Bytes, protectedBytes
    outputBytes = [b'\x00'] * len(remasterBytes)

    # Iterate through all the bytes
    for address in range(len(remasterBytes)):

        # The address is flagged in the protected bytes list
        # No change to the original file is made
        if(address in protectedBytes):
            outputBytes[address] = remasterBytes[address]

        # All three files are the same so no change was made
        elif((remasterBytes[address] == redux1Bytes[address]) and
                (remasterBytes[address] == redux2Bytes[address])):
            outputBytes[address] = remasterBytes[address]

        # Take changes from redux1
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] == redux2Bytes[address])):
            outputBytes[address] = redux1Bytes[address]

        # Take changes from redux2
        elif((remasterBytes[address] == redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address])):
            outputBytes[address] = redux2Bytes[address]

        # Both files differ from the remaster but both contain the same data
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address]) and
                (redux1Bytes[address] == redux2Bytes[address])):
            outputBytes[address] = redux1Bytes[address]

        # Both files are diffrent and the redux files dont align either
        # this should never happen
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address]) and
                (redux1Bytes[address] != redux2Bytes[address])):
            print("This should never happen address: " + str(address))
            outputBytes[address] = remasterBytes[address]

    return outputBytes


populateByteLists()

outputList = performChanges()

# Write the binary information to new output file
with open("TestFileStructure/output_M_DAT.BIN", 'wb+') as outputFile:
    for byte in outputList:
        tmp = byte.to_bytes(1, 'big')
        outputFile.write(tmp)
