import operator
import csv
import matplotlib.pyplot as plt
import numpy as np 

dict = {}
#with open('avspeech_train.csv', newline='') as csvfile:
with open('avspeech_train.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
       cur = row[0].split(',')[0] 
       if cur in dict.keys():
           dict[cur] = dict[cur] + 1
       else: 
           dict[cur] = 1

print(max(dict.items(), key=operator.itemgetter(1)))
x = np.arange(81)
y = np.zeros(81)
for key in dict:
    y[dict[key]] += 1
for i in range(81):
    print(str(int(x[i])) + ':', int(y[i])) 
