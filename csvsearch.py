import csv
with open('testcsv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        if row == ['3DP,1.1.1']:
            location = "1.1.1";
            

    
