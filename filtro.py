import csv
import re

pattern = re.compile(r'^(\d{4,4})\-(\d{2,2}\-?){2},(.*),Colombia.*Friendly.*$')
cont = 1

with open("/home/joseph/home/Documentos/Programación/data/matches.csv", "r") as f:
    for i in f:
        match_pattern = re.match(pattern,i)
        if match_pattern:
            print(f"{cont} partido de {match_pattern.group(1)}: {i}\n")
            cont += 1