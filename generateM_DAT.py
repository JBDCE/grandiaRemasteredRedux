

REMASTER_MDAT = open("TestFileStructure/original_M_DAT.BIN", 'rb')
REDUX1_MDAT = open("TestFileStructure/redux1_M_DAT.BIN", 'rb')
REDUX2_MDAT = open("TestFileStructure/redux2_M_DAT.BIN", 'rb')


redux1Bytes = []
redux2Bytes = []
remasterBytes = []


def populateByteLists():
    global remasterBytes, redux1Bytes, redux2Bytes

    remasterBytes = bytearray(REMASTER_MDAT.read())
    # the three files should all be equal in length

    redux1Bytes = bytearray(REDUX1_MDAT.read())
    assert len(redux1Bytes) == len(remasterBytes), "Redux1_MDAT is the wrong length"

    redux2Bytes = bytearray(REDUX2_MDAT.read())
    assert len(redux2Bytes) == len(remasterBytes), "Redux1_MDAT is the wrong length"

    print("Remaster lenght: " + str(len(remasterBytes)))


def getString(barray, address):
    value = ""
    #  for i in range(-4, 6, 1):
    #      value += chr(barray[address + i])

    # Find End of the current Text
    i = 0
    end = ''
    while barray[address + i] > 31:
        end += chr(barray[address + i])
        i += 1

    # Find beginning of current Text^
    i = -1
    beginning = ''
    while barray[address + i] > 31:
        beginning += chr(barray[address + i])
        i -= 1

    value = beginning[::-1] + end

    return value


def performComparison():
    global remasterBytes, redux1Bytes, redux2Bytes
    outputBytes = [b'\x00'] * len(remasterBytes)


    i = 0
    j = 0

    register = []
    # Iterate through all the bytes
    for address in range(len(remasterBytes)):


        # All three files are the same so no change was made
        if((remasterBytes[address] == redux1Bytes[address]) and
                (remasterBytes[address] == redux2Bytes[address])):
            outputBytes[address] = remasterBytes[address]

        # Take changes from redux1
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] == redux2Bytes[address])):
            outputBytes[address] = redux1Bytes[address]

            if (outputBytes[address] > 65 and outputBytes[address] < 90) or (outputBytes[address] > 97 and outputBytes[address] < 122):
                j += 1
                if j == 4:
                    i += 1
                    register.append({
                        'address': hex(address),
                        'sourceFile': "redux1", 
                        'original:': getString(remasterBytes, address),
                        'redux': getString(redux1Bytes, address)
                        }
                    )
            else:
                j = 0

        # Take changes from redux2
        elif((remasterBytes[address] == redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address])):
            outputBytes[address] = redux2Bytes[address]

            if (outputBytes[address] > 65 and outputBytes[address] < 90) or (outputBytes[address] > 97 and outputBytes[address] < 122):
                j += 1
                if j == 4:
                    i += 1
                    register.append({
                        'address': hex(address),
                        'sourceFile': "redux2", 
                        'original:': getString(remasterBytes, address),
                        'redux': getString(redux2Bytes, address)
                        }
                    )
            else:
                j = 0

        # Both files differ from the remaster but both contain the same data
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address]) and
                (redux1Bytes[address] == redux2Bytes[address])):
            outputBytes[address] = redux1Bytes[address]

            if (outputBytes[address] > 65 and outputBytes[address] < 90) or (outputBytes[address] > 97 and outputBytes[address] < 122):
                j += 1
                if j == 4:
                    i += 1
                    register.append({
                        'address': hex(address),
                        'sourceFile': "redux1", 
                        'original:': getString(remasterBytes, address),
                        'redux': getString(redux1Bytes, address)
                        }
                    )
            else:
                j = 0

        # Both files are diffrent and the redux files dont align either
        # this should never happen
        elif((remasterBytes[address] != redux1Bytes[address]) and
                (remasterBytes[address] != redux2Bytes[address]) and
                (redux1Bytes[address] != redux2Bytes[address])):
            print("This should never happen address: " + str(address))
            outputBytes[address] = remasterBytes[address]
    print(i)
    return outputBytes


populateByteLists()

outputList = performComparison()

# Write the binary information to new output file
with open("output_M_DAT.BIN", 'wb+') as outputFile:
    for byte in outputList:
        tmp = byte.to_bytes(1, 'big')
        outputFile.write(tmp)
