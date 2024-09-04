#symbol paste

text = input(f"Please enter your text: ").rstrip().lstrip()
symbol = input(f"Please enter your symbol( * - ^ ~ ' , . ): ")

edited_text = symbol.join(text.replace(" " , symbol))       #join the each character with user choosen symbol and remove spaces

print(f"Your word with symbols: ", edited_text)
