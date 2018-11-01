# gba_savetypes
A quick and dirty Python3 script (not so "pythonish") to list GBA (Game Boy Advance) games which use a certain type of save.

# Usage 
./gba_savetype.py [-h] {savetype}

Example:
./gba_savetype.py NONE

If no argument is passed to the script, the script lists in the usage block the savetypes present in the file .
Example:
 ./gba_savetype.py 
usage: gba_savetype.py [-h] {EEPROM,FLASH,FLASH1M,FLASH512,NONE,SRAM}
gba_savetype.py: error: the following arguments are required: savetype

# Requirement
The XML file gba_OL.xml which describe every GBA games is required. 
It comes from http://offlinelist.free.fr/ (thanks to Replouf66).
