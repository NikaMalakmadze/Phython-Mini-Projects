#Task from codeforces

con1 = input(f"Please enter your text: ").lower()           #lowercase all letters
con2 = con1.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("y", "")   #remove all vowels
con3 = con2.replace("", ".")        #put a dot before a consonant letter

print(f"output: ", con3[0 : -1])         #remove the extra dot at the end