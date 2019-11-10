import json
from collections import defaultdict
from sortedcontainers import SortedDict

"""
 * @author Henry Guo on 11/08/19.
 * @project HackUtd
 * @email hxg190003@utdallas.edu
 * @organization UTDallas
"""


def txt2list(filepath):
    txtfile = open(filepath, 'r')
    txtline = txtfile.readlines()
    txtfile.close()
    return txtline


symptomsList = txt2list("SymptomsList.txt")
# Default a dictionary to same symptoms' number
symptomsDictionary = defaultdict(float)

# Count symptoms number and save it into dictionary
for symptoms in symptomsList:
    print(symptoms.split()[0])
    symptomsDictionary[symptoms.replace(' ', '_').split()[0]] += 1

# Change each count number into its reciprocal
for symptomsNum in symptomsDictionary:
    symptomsDictionary[symptomsNum] = 1/symptomsDictionary[symptomsNum]

# Sort dictionary with its alphabet
sortedSymptomsDictionary = SortedDict(symptomsDictionary)

# Save symptoms and its reciprocal number
with open('SymptomsCount.json', 'w') as outfile:
    json.dump(sortedSymptomsDictionary, outfile)