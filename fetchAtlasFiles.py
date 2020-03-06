
import argparse
from shutil import copy
from os import getcwd, path

# Parser stuff that took way too long to figure out...
parser = argparse.ArgumentParser()

parser.add_argument(
    "--path",
    dest="gamepath",
    help="Point this to the GRANDIA folder on your hard drive",
    action="store"
)
args = parser.parse_args()

# Fields for which files to get
resourcePath = "content/FIELD/"
atlasFileEnding = "*__atlas.png"

saveFolder = "/atlasFiles"

# Prepare the needed paths using the pathlib library

rawSource = args.gamepath + resourcePath + atlasFileEnding
rawDestination = getcwd() + saveFolder

source = path.normpath(rawSource)
destination = path.normpath(rawDestination)

print("Source: " + str(source))
print("Final Destination " + str(destination))

# actual file copy command that was a single line in cmd
copy(source, destination)
