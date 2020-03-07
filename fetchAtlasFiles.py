import argparse
from os import getcwd, path, mkdir, listdir
import subprocess

# Parser stuff that took way too long to figure out...
parser = argparse.ArgumentParser()

parser.add_argument(
    "--source",
    "-s",
    dest="sourcepath",
    help="Point this to the GRANDIA folder on your hard drive",
    action="store"
)

parser.add_argument(
    "--destination",
    "-d",
    dest="destinationpath",
    help="Point this to the desired output folder",
    action="store"
)

parser.add_argument(
    "--pattern",
    "-p",
    dest="filePattern",
    help="Input the filter pattern",
    action="store"
)

# parser.add_help = True
args = parser.parse_args()

atlasFilePattern = "*" + args.filePattern

saveFolder = getcwd() + args.destinationpath

rawSource = args.sourcepath + atlasFilePattern
rawDestination = saveFolder

# Prepare the needed paths using the pathlib library
source = path.normpath(rawSource)

# "\\" is needed so the path points to a windows folder
destination = path.normpath(rawDestination) + "\\"


# Print the information for debugging
print("Source: " + str(source))
print("Final Destination: " + str(destination))

# TODO Check if Paths exist
# assert path.isfile(source), "Source Path invalid"
# assert path.isdir(destination), "Destination Path invalid"

# Create destination folder if it doesnt exist
try:
    mkdir(destination)
except FileExistsError:
    print("Destination Path already exists..")
    assert len(listdir(destination)) == 0, "Destination Path needs to be empty"

# actual file copy command that was a single line in cmd
subprocess.run(["copy", source, destination], shell=True)
