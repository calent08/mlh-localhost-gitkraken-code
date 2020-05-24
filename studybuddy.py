import csv
import os
search_for = ['chrome.exe']
os.system("tasklist /fo csv > study_bud.txt")
with open('study_bud.txt') as f:
     reader = csv.reader(f, delimiter=",")
     for row in reader:
          if row[0] in search_for:
               print("\nPlease close: ", row[0], "\n")
               exit(0)
