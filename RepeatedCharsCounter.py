## Author: Feras Isied
##  Problem: A function that returns a list of characters that
##  has at least two occurrences                                                 

userInput = str(input("Enter a string:\n"))
def repeatedChar(string):
    repeatedLst = []
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            if string[i] not in repeatedLst:
                repeatedLst.append(string[i])
    return repeatedLst
print(repeatedChar(userInput))