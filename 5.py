#import csv
#with open('sample.csv', newline='') as csvfile:
 #   reader = csv.reader(csvfile)
 #   for row in reader:
 #       print(row)

#ls = [1,2,3,4]
#first_elem = next(ls)
#print(first_elem)

#grocery store problem the can chooes the item


import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['Rice', '100 '])
    spamwriter.writerow(['wheat', '200'])
    spamwriter.writerow(['oil', '300'])