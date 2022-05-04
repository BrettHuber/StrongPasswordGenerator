import random

specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "?", "<", ">", "/", "|", "`", "~", ";", ":", ",", ".", "-", "+", "="]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
capitalLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

minLength = 12
maxLength = 24
 
strongPassword = ""
passwordLength = random.randrange(12,25)

for x in range(passwordLength):
    if(x == 1):
        charNum = random.randrange(0, len(capitalLetters) + 1)
        strongPassword += capitalLetters[charNum]
    elif(x % 5 == 0):
        charNum = random.randrange(0, len(capitalLetters) + 1)
        strongPassword += capitalLetters[charNum] 
    elif(x % 4 == 0):
        charNum = random.randrange(0, len(numbers) + 1)
        strongPassword += numbers[charNum]
    elif(x % 3 == 0):
        charNum = random.randrange(0, len(letters) + 1)
        strongPassword += letters[charNum] 
    elif(x % 2 == 0 or x % 7 == 0):
        charNum = random.randrange(0, len(specialCharacters) + 1)
        strongPassword += specialCharacters[charNum]
    else:
        charNum = random.randrange(0, len(letters) + 1)
        strongPassword += letters[charNum] 






