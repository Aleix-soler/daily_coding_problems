import array
import random

#Variables
iArray = []
fArray = []

#Load initial array with numbers
def loadArray():
    for i in range(8):
        iArray.append(i+1)
        #iArray.append(random.randint(1,9))

#Load final array with all the values multiplied except the actual one
def calculateArray():
    for i in range(len(iArray)):
        finalNumber = 1
        for j in range(len(iArray)):
            if j==i:
                continue

            finalNumber = finalNumber*iArray[j]
        fArray.append(finalNumber)

def printArrays():
    print(iArray)
    print(fArray)

loadArray()
calculateArray()
printArrays()
