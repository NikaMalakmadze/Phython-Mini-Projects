#Easy or Hard |CodeForces task|

coordinator_num = int(input("Please enter people number: "))                                  #get number of Codeforce Coordinators
response = (input("Please enter task difficuly with spaces (0 if EASY|1 if HARD)"))           #find out the opinion of each coordinator about the task

list = response.split()                 #put each response in one list

if len(list) == coordinator_num:                 #check if coordinator number equal to responses number
    if list.count("1") >= 1 :                       #if "1" is in a list at least one time,then it's HARD task
        print("     Tast is: |HARD|")
        print(f"Result of review: {list}")          #additionaly print Result of reviews
    else:                                           #if not it's EASY task
        print("     Task is: |EASY|")               
        print(f"Result of review: {list}")          #additionaly print Result of reviews
else:                                               #if coordinator number don't equal to responses number
   print("ERROR!")
