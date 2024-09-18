#Practice |number information 2.0|

num = int(input())          #get number from user

numList = []                #create empty list

num_digit_count = 0         
num_digit_mult = 1
num_digit_sum = 0

max_digit = 0

min_digit = 9

even_digit = 0
odd_digit = 0

str_num = str(num)          #convert number from int to string and store it in new variable

if str_num == str_num[ : : -1]:         #check if number is palindromic
    answer = "Palindromic"
else:
    answer = "Non-Palindromic"

while num > 0:                          
    num_digit_count += 1
    last_digit = num % 10

    if last_digit % 2 == 0:             #check if digit is even
        even_digit += 1
    else:
        odd_digit += 1

    if last_digit > max_digit:          #search for biggest digit
        max_digit = last_digit

    if last_digit < min_digit:          #search for smallest digit
        min_digit = last_digit

    num_digit_mult *= last_digit           #multiply of all digits
    num_digit_sum += last_digit            #sum of all digits

    numList.append(last_digit)             #add every digit in list
    
    num = num // 10                        

num_digit_average = round(sum(numList) / num_digit_count , 2)       #get average of digits in number and round it to hundreds

numList.reverse()                           #reverse list

#print info

print(numList)
print(f"count of digits in your number: {num_digit_count}")
print(f"count of even digits in your number: {even_digit}")
print(f"count of odd digits in your number: {odd_digit}")
print(f"sum of digits in your number: {num_digit_sum}")
print(f"multiply of digits in your number: {num_digit_mult}")
print(f"min digit in your number: {min_digit}")
print(f"max digit in your number: {max_digit}")
print(f"average digit in your number: {num_digit_average}")
print(f"is your number palindromic? answer: {answer}")
