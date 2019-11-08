from random import seed, randint, randrange

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


# seed random number generator
seed(1)

# Read Doctor Majors file
generateDocMajor = []
docLine = txt2list('DoctorMajors.txt')
for _ in range(100):
    randomDoctorMajorNum = randrange(0, 120, 2)
    generateDocMajor.append(docLine[randomDoctorMajorNum].strip())

# Read Top 100 Names in the USA
generateDocName = []
generateDocGender = []
topName = txt2list("Top100Names.txt")
for _ in range(100):
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
for _ in range(100):
    randomStateNum = randint(0, 47)
    generateStateName.append(stateList[randomStateNum].strip())

# Generate seniority of each doctor
generateSeniority = []
for _ in range(100):
    randomSeniorityNum = randint(0, 20)
    generateSeniority.append(randomSeniorityNum)

for i in range(100):
    print(generateDocMajor[i])
    print(generateDocName[i])
    print(generateDocGender[i])
    print(generateStateName[i])
    print(generateSeniority[i])