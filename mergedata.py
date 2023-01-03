import csv
import pandas as pd

dataset1 = []
dataset2 = []

with open("proj127.csv", "r", encoding = "utf8")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("converted_dwarf.csv", "r", encoding = "utf8") as f:
    csvreader= csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

h1 = dataset1[0]
h2 = dataset2[0]

star_data1 = dataset1[1:]
star_data2 = dataset2[1:]

star_data = []

for row in star_data1:
    star_data.append(row)

for row in star_data2:
    star_data.append(row)

with open("total_stars.csv", "w", encoding = "utf8", newline = "")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h1)
    csvwriter.writerows(star_data)

