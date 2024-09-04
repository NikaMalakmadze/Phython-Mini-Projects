#word counter in a text

text = input(f"Please enter yout text: ").rstrip()      #receive input text an remove spaces from the end of text

wordnum = len(text.split())         #split the text by spaces and put it in the list.then get the number of elements in that list.store it as a int

print(f"Word number in your text is: ", wordnum)    #print word count 
