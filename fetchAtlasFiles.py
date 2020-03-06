import argparse
from os import getcwd, path
import subprocess

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
atlasFilePattern = "*__atlas.png"

saveFolder = "/atlasFiles/"

# Prepare the needed paths using the pathlib library
rawSource = args.gamepath + resourcePath + atlasFilePattern
rawDestination = getcwd() + saveFolder

fileNames = []

source = path.normpath(rawSource)
destination = path.normpath(rawDestination) + "\\"

print("Source: " + str(source))
print("Final Destination " + str(destination))

# actual file copy command that was a single line in cmd

subprocess.run(["copy", source, destination], shell=True)
