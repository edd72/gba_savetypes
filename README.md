# gba_savetypes
A quick and dirty Python3 script (not very "pythonish") to list GBA (Game Boy Advance) games which use a certain type of save.

# Usage 
./gba_savetype.py [-h] {savetype}

If no argument are passed to the script, the savetypes present in the file are listed.
Example:
 ./gba_savetype.py 
usage: gba_savetype.py [-h] {EEPROM,FLASH,FLASH1M,FLASH512,NONE,SRAM}
gba_savetype.py: error: the following arguments are required: savetype

# Requirement
The XML file gba_OL.xml which describe every GBA games is required. 
It comes from http://offlinelist.free.fr/ (thanks to Replouf66).
