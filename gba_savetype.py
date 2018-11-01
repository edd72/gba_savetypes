#!/usr/local/bin/python3

# vim: set fileencoding=utf-8

import xml.etree.ElementTree as ET
import argparse
import sys

#-- vars
titr = []
sauv = []
scod = []
pays = []

#-- Chargement listes
def charge_listes():
    try:    
        tree = ET.parse('gba_OL.xml')
    except:
        print("Cannot read the OfflineList file gba_OL.xml")
        sys.exit(1)
    else:
        root = tree.getroot()
        games = root.find('games')
        for game in games.findall('game'):
            titr.append(game.find('title').text)
            sauv.append(game.find('saveType').text)
            #-- première partie avant le _ puis upper
            scod.append(game.find('saveType').text.split('_')[0].upper())
            pays.append(game.find('location').text)

#-- Charge la liste résultat
def alim_jeux(savetype,liste_res):
    for index_lu,savetype_lu in enumerate(scod):
        if (savetype_lu == savetype):
           liste_res.append(titr[index_lu])

#-- LET'S GO
def main():
    charge_listes()

    #-- parser tardif (détermination des types connus avant)
    parser = argparse.ArgumentParser()
    parser.add_argument("savetype", choices=sorted(list(set(scod))), help="savetypes known")
    args = parser.parse_args()

    jeux_res = []

    alim_jeux(args.savetype, jeux_res)

    print (f"Games with save of type {args.savetype}:")
    print (f"-----------------------------")
    #-- dedoub. (set) + tri
    for jeu in sorted(list(set(jeux_res))):
        print(jeu)

main()
