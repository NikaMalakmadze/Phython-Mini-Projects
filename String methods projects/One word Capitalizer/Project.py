#One word Capitalizer

text = input(f"Please enter one word: ")

first_char = text[0].capitalize()       #capitalizing Only the first letter of the word by its index |P.S| works with the upper method too

print(f"Capitalized word: ", first_char + text[1 : ])       # adding remaining letters to the first letter
