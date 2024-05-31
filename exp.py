import csv

filename = "hand_data.csv"

csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile)

csvwriter.writerow([(230,12),(21,212), (232, 242)])