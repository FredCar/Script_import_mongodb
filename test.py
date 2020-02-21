import read_tsv as tsv
import DBInteract as dbi
import Modifieur as mod
import pprint


# Lecture du fichier TSV
tsv = tsv.TsvReader('../data/mon_fichier.tsv') # Chemin du fichier à traiter
  
# Connection à la base      
host = "localhost"
port = 27017
base = "test_movies"
collec = "test_test"

ma_base = dbi.DBInteract(host, port, base, collec)

mod = mod.Modifieur()

liste = []
while True:
    lines = tsv.read_seq(1000)

    if lines == "":
        break

    for x in lines:
        x = mod.spliter(x, key="primaryProfession")
        x = mod.spliter(x, key="knownForTitles")
        x = mod.integer(x, key="birthYear")
        x = mod.integer(x, key="deathYear")
        liste.append(x)
        
        if len(liste) >= 10:
            ma_base.insert(liste, method="many")
            liste = []

    
 
    
    
