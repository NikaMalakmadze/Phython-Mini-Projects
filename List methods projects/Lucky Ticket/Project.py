#Lucky Ticket |Task from ACMP.ru|

#Task condition:
#A lucky ticket is a ticket whose sum of the first part of the number digits is equal to the sum of the second part of number digits
#However, the length of the ticket number must be even

#lucky ticket example: 123321       unlucky ticket example: 123456

# |Task solution:| #

#getting number from user

number = input()

if len(number) % 2 == 0:                                #checking if ticket number length is even

    #splitting number into two parts

    first_part = number[ : len(number) // 2 ]                   #first part of the ticket number
    last_part = number[len(number) // 2 : ]                     #last part of the ticket number

    first_part_digit_list = first_part.replace("", " ").split()         #store the first part of the ticket number digits in first list
    last_part_digit_list = last_part.replace("", " ").split()           #store the last part of the ticket number digits in second list

    first_part_digit_list = map(int, first_part_digit_list)               #converting every digit of list from string into int
    sum1 = sum(first_part_digit_list)                                     #The sum of the first part of the ticket number digits

    last_part_digit_list = map(int, last_part_digit_list)                 #converting every digit of list from string into int
    sum2 = sum(last_part_digit_list)                                      #The sum of the last part of the ticket number digits

    #checking whether the ticket is lucky or not

    if sum1 == sum2:
        print("Your Ticket is LUCKY")
    else:
        print("Your Ticket is UNLUCKY")

else:
     print("Your Ticket is UNLUCKY")
