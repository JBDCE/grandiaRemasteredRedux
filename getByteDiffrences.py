# import json

ORIGINAL_MDAT = open("original_M_DAT.BIN", 'rb')
REDUX_MDAT = open("redux1_M_DAT.BIN", 'rb')


differences = []

previousByteWasDiffrent = False
currentPosition = 0

while True:
    orignal_byte = ORIGINAL_MDAT.read(1)
    redux_byte = REDUX_MDAT.read(1)

    # Exit the Loop if the end of either file is reached
    if (not orignal_byte) or (not redux_byte):
        break

    # Check for zero byte
    if(orignal_byte == b'\x00' and
            redux_byte == b'\x00' and
            previousByteWasDiffrent):

        tmp = differences[len(differences) - 1]
        tmp["end"] = currentPosition + 1
        tmp["length"] += 1
        tmp["original_data"].append(orignal_byte)
        tmp["redux_data"].append(redux_byte)
        differences[len(differences) - 1] = tmp
        previousByteWasDiffrent = True

    if(orignal_byte != redux_byte):

        if not previousByteWasDiffrent:
            differences.append(
                {
                    "start": currentPosition,
                    "end": currentPosition + 1,
                    "length": 1,
                    "original_data": [orignal_byte, ],
                    "redux_data": [redux_byte, ]
                }
            )
            previousByteWasDiffrent = True
        # Extend the previous entry if the next diffrence is right next to it
        else:
            tmp = differences[len(differences) - 1]
            tmp["end"] = currentPosition + 1
            tmp["length"] += 1
            tmp["original_data"].append(orignal_byte)
            tmp["redux_data"].append(redux_byte)
            differences[len(differences) - 1] = tmp

    # Equal byte in both files
    else:
        previousByteWasDiffrent = False

    currentPosition += 1

# Write to output file
with open("differences.out", 'w+') as outputFile:
    for diff in differences:
        print(str(diff))
        outputFile.write(str(diff))
        outputFile.write("\n")
