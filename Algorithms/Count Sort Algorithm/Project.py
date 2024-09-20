#Count sort Algorithm|Text sort|

#sorting letters in alphabetical order | sorting digits in a acsending order | dont sorting symbols

#some decorations

print("")
print("------------------SORTING-PROGRAM-------------------------")
word = input("Please input unsorted text: ").replace(" ", "")                               #getting text from user
print("------------------SORTING-PROGRAM-------------------------")

letters = [0] * 26              #create a 26-place list where each letter has its own place

digits = [0] * 10               #create a 10-place list where each digit has its own place

symbol = []                     #create empty list for symbols

for char in word.lower():                     #using for loop to check each character in user text
    if char >= "a" and char <= "z":                     #check if its letter
        number = ord(char) - 97                           #give each letter its own number to store it in a list |for example: "a" = 97 - 97 = 0|
        letters[number] += 1                                #store each letter in letters list with its own number(nomer) |count it|
    elif char >= "0" and char <= "9":               #check if its digit
        digit_number = ord(char) - 48                 #give each digit its own number to store it in a list | for example: "0" = 48 - 48 = 0|
        digits[digit_number] += 1                       #store each digit in digits list with its own number(nomer) |count it|
    else:
        symbol.append(char)                           #put everything else in symbol list

#some decorations

print("")
print("---------------------------RESULT-------------------------")
print("Sorted text: ", end="")

for letter in range(26):                                                    #using for loop to convert each number(nomer) back to letter
    if letters[letter] > 0:                                                     #check if letter is in a letters list
        print(chr(letter + 97) * letters[letter] , end="")                              #convert number to letter and multipy it on its count

for digit in range(10):                                                     #using for loop to convert each number(nomer) back to digit
    if digits[digit] > 0:                                                       #check if digit is in a digits list
        print(chr(digit + 48) * digits[digit] , end="")                                 #convert number to digit and multipy it on its count

print("".join(symbol))                                                          #add symbols at the end without sorting
print("---------------------------RESULT-------------------------")
print("")
