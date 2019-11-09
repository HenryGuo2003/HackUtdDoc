from random import seed, randint, randrange
import random

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
generateDocMajor = []
docLine = txt2list('DoctorMajorSymptoms.txt')
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
    generateDocMajor.append('')
    for randNum in resultRandomNum:
        generateDocMajor[i] = generateDocMajor[i] + (docLine[randNum].strip()) + ','
    generateDocMajor[i] = generateDocMajor[i][:-1]

# Read Top 100 Names in the USA
generateDocName = []
generateDocGender = []
topName = txt2list("Top100Names.txt")
for _ in range(DocNum):
    randomNameNum = randint(0, 199)
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

for i in range(DocNum):
    print(generateDocMajor[i])
    print(generateDocName[i])
    print(generateDocGender[i])
    print(generateStateName[i])
    print(generateSeniority[i])
    print(generatePhoneNumber[i])