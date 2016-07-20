import csv

f = open('test.csv', 'w')
writer = csv.writer(f, lineterminator="\n")
writer.writerow(['I', 'love', 'lamp'])
writer.writerow([1,2,3])
f.close()