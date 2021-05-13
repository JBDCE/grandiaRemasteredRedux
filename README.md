# Grandia Remastered Redux

This is a repository for the port of Grandia Redux into the 2019 Released Grandia HD Remaster

# Important Note
None of this is anywhere near stable and currently not working. Main issue with the progress is that the characters still get their old spells unlocked instead of the Redux ones. Any help on this is greatly appreciated.

# Installing from Release
If you only care about playing the game in the Redux version you can just download the latest release extract the files over folder of the Games download path. 
Make sure that you backup your save files first as I take no responsibility in you loosing your game files.
Your saves on Windows are Located in: ```%APPDATA%/GRANDIA1```

# Requirements for Recreation:
- The Steam version of the HD Remaster
- ISO Rips from the Original North American Playstation 1 Release of the Game
- PPF Patch files from Grandia Redux

**This entire process is pretty unstable at this stage and I would not suggest anyone to recreate it. But in case anyone wants to reinact this (and so I dont forget 2 years down the line).**

Also just as a disclaimer I mainly used Windows for this so all the Software Im suggesting is tailored towards my workflow there are surely fitting Linux alternatives for all this. If you want to suggest software alternatives for me to include them into here just write me a message.

## Preparation
Patch the original games two Iso files using a software like [ppf-o-matic](http://www.romhacking.net/utilities/356/) together with the .ppf files. Im including these two rar Archives with this repository since the original downloads dont seem to exist anymore.

Mount the patched Iso Files with software like [Virtual Clone Drive](https://www.elby.ch/en/products/vcd.html)

Extract the files from the disks into seperate Folders like this:
```
TestFileStructure
+---ReduxGameFiles
|   +---DISK1
|   |   +---BATLE
|   |   +---BIN
|   |   \---FIELD
|   \---DISK2
|       +---BATLE
|       +---BIN
|       \---FIELD
```
Just copy over the Folders doing what we are about to do does not need the files inside the root directory

Next to this you want to create a folder called **RemasterGameFiles** and copy over the content file structure. You dont actually need all the files. Just the subfolder TEXT but its important that the structure stays the same.

Your **TestFileStructure** folder should now look something like this:
```
TestFileStructure
+---ReduxGameFiles
|   +---DISK1
|   |   +---BATLE
|   |   +---BIN
|   |   \---FIELD
|   \---DISK2
|       +---BATLE
|       +---BIN
|       \---FIELD
\---RemasterGameFiles
    \---TEXT
```

## The easy parts

Since the HD version is just a glorified PS1 Game you can copy some files straight over into the content Folder of the Remaster. 

From Disk 1:
BIN/MCHAR.DAT
FIELD/SHOP.BIN

From Disk 2:
FIELD/WINDT.BIN

## Using the hex editor

Some files got split into multiple ones during the translation part of the remaster. This means that you need to extract the item descriptions from within other files.




## Using the Code
You will mainly need the generateM_DAT.py and extractText.py file for creating the BATLE/M_DAT.BIN file together with most of the text files from the TEXT subfolder.

Create a folder called **TestFileStructure** next to the generateM_DAT.py and ex<span>tractText.p</span>y
Open the mounted original Redux Disk 1
Copy over the file BATLE/M_DAT.BIN into the **TestFileStructure** folder you created and rename it into **redux1_M_DAT.BIN**

Open the mounted original Redux Disk 2 next
Copy over the file BATLE/M_DAT.BIN into the **TestFileStructure** folder you created and rename it into **redux2_M_DAT.BIN**

Go into the remasters game files and copy the content/BATLE/M_DAT.BIN file as well as the content/TEXT/strings.txt
Rename those into original_M_DAT.BIN and original_strings.txt respectively.

Lastly From the repository files copy over the names.txt file into the **TestFileStructure* folder

If you collected all that run the generateM_DAT.py software. It should take a couple of minutes and generate two files: the output_M_DAT.BIN as well as the output_strings.txt



## Fixing up the Result

