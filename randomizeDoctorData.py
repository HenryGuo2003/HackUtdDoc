from random import seed, randint, randrange
import random
import json
from collections import defaultdict

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


DocNum = 100

# seed random number generator
seed(1)

# Read Doctor Majors file
resultRandomNum = []
generateDocMajorSymptoms = []  # Doctors' detail major symptoms
generateDocMajor = []  # Doctors' major department
generateMajorRank = []  # Doctors' rank number of each major
docLine = txt2list('DoctorMajorSymptoms.txt')
docMajorLine = txt2list('DoctorMajors.txt')
for i in range(DocNum):
    randomDeptNum = randint(1, 4)
    randomDoctorMajorNum = randint(1, 3)
    if randomDeptNum == 1:
        resultRandomNum = random.sample(range(0, 4), randomDoctorMajorNum)
    elif randomDeptNum == 2:
        resultRandomNum = random.sample(range(6, 10), randomDoctorMajorNum)
    elif randomDeptNum == 3:
        resultRandomNum = random.sample(range(12, 18), randomDoctorMajorNum)
    elif randomDeptNum == 4:
        resultRandomNum = random.sample(range(20, 24), randomDoctorMajorNum)
    elif randomDeptNum == 5:
        resultRandomNum = random.sample(range(26, 30), randomDoctorMajorNum)
    elif randomDeptNum == 6:
        resultRandomNum = random.sample(range(32, 34), randomDoctorMajorNum)
    generateDocMajor.append(docMajorLine[randomDeptNum-1].strip())  # Save random major department into generateDocMajor
    generateDocMajorSymptoms.append('')
    for randNum in resultRandomNum:
        generateDocMajorSymptoms[i] = generateDocMajorSymptoms[i] + (docLine[randNum].strip()) + ','
    generateDocMajorSymptoms[i] = generateDocMajorSymptoms[i][:-1]
    # Generate rank number
    generateMajorRank.append('')
    for _ in range(randomDoctorMajorNum):
        generateMajorRank[i] = generateMajorRank[i] + str(randint(1, 10)) + ','
    generateMajorRank[i] = generateMajorRank[i][:-1]

# Read Top 100 Names in the USA
generateDocName = []
generateDocGender = []
topName = txt2list("Top100Names.txt")
randomNameNumList = random.sample(range(0, 199), DocNum)
for randomNameNum in randomNameNumList:
    if randomNameNum >= 100:
        generateDocGender.append('FeMale')
        generateDocName.append(topName[randomNameNum-100].strip().split(' ')[2])
    else:
        generateDocGender.append('Male')
        generateDocName.append(topName[randomNameNum].strip().split(' ')[1])

# Read State Name list in the USA
generateStateName = []
stateList = txt2list("ListOfStateName.txt")
for _ in range(DocNum):
    randomStateNum = randint(0, 47)
    generateStateName.append(stateList[randomStateNum].strip())

# Generate seniority of each doctor
generateSeniority = []
for _ in range(DocNum):
    randomSeniorityNum = randint(0, 20)
    generateSeniority.append(randomSeniorityNum)

# Generate phone number of each doctor
generatePhoneNumber = []
phoneList = txt2list("RandomPhoneNumber.txt")
for _ in range(DocNum):
    randomPhoneNumber = randrange(0, 398, 4)
    generatePhoneNumber.append(phoneList[randomPhoneNumber].strip())

# Save generate data as json file
docDictionary = defaultdict(list)
for i in range(DocNum):
    docDictionary[generateDocName[i]] = []
    docDictionary[generateDocName[i]].append({
        'Gender': generateDocGender[i],
        'Major': generateDocMajor[i],
        'Symptoms': generateDocMajorSymptoms[i],
        'Rating': generateMajorRank[i],
        'Seniority': generateSeniority[i],
        'Location': generateStateName[i],
        'PhoneNumber': generatePhoneNumber[i]
    })

with open('DocDictionary.json', 'w') as outfile:
    json.dump(docDictionary, outfile)