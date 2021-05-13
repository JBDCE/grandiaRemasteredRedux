import sys
# Read the args

assert len(sys.argv)==6, \
    "Usage: python3 3FileMerge.py [path_to_original] [path_to_fileB] [path_to_fileC] [Output file] [conflict handle]\n" + \
        "Conflict handle Syntax:\n1 for take from original\n2 for take from B\n3 for take from C"

filePathOriginal = sys.argv[1]
filePath_B = sys.argv[2]
filePath_C = sys.argv[3]
filePathOutput = sys.argv[4]
onConflict = sys.argv[5]

# Load the files into bytearrays
with open(filePathOriginal, 'rb') as A:
    bytesOriginal = bytearray(A.read())
with open(filePath_B, 'rb') as B:
    bytesB = bytearray(B.read())
with open(filePath_C, 'rb') as C:
    bytesC = bytearray(C.read())

# Validate they are the same length
assert len(bytesB) == len(bytesOriginal),\
     "File B (" + len(bytesB) + ") is the Wrong Length. Should be: " + len(bytesOriginal)
assert len(bytesC) == len(bytesOriginal),\
     "File C (" + len(bytesC) + ") is the Wrong Length. Should be: " + len(bytesOriginal)

print("Length Check Successful")
print("Original File length: " + len(bytesOriginal))

# Perform the changes 
outputBytes = [b'\x00'] * len(bytesOriginal)

for address in range(len(bytesOriginal)):

    # All three files are the same so no change was made
    if((bytesOriginal[address] == bytesB[address]) and
            (bytesOriginal[address] == bytesC[address])):
        outputBytes[address] = bytesOriginal[address]

    # Take changes from bytesB
    elif((bytesOriginal[address] != bytesB[address]) and
            (bytesOriginal[address] == bytesC[address])):
        outputBytes[address] = bytesB[address]

    # Take changes from bytesC
    elif((bytesOriginal[address] == bytesB[address]) and
            (bytesOriginal[address] != bytesC[address])):
        outputBytes[address] = bytesC[address]

    # Both files differ from the original but both contain the same data
    elif((bytesOriginal[address] != bytesB[address]) and
            (bytesOriginal[address] != bytesC[address]) and
            (bytesB[address] == bytesC[address])):
        outputBytes[address] = bytesB[address]

    # All 3 files missalign
    elif((bytesOriginal[address] != bytesB[address]) and
            (bytesOriginal[address] != bytesC[address]) and
            (bytesB[address] != bytesC[address])):

        print("All 3 differ from Eachother")
        print("Address: " + address)
        print("Original: " + bytesOriginal[address])
        print("BytesB: " + bytesB[address])
        print("BytesC: " + bytesC[address])

        if onConflict==1:
            outputBytes[address] = bytesOriginal[address]
        elif onConflict==2:
            outputBytes[address] = bytesB[address]
        elif onConflict==3:
            outputBytes[address] = bytesC[address]

# Write an output File
with open(filePathOutput, 'wb+') as outputFile:
    for byte in outputBytes:
        tmp = byte.to_bytes(1, 'big')
        outputFile.write(tmp)
