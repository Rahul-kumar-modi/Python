#Write a program to fill in a letter template give below with name and date.

letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Rahul").replace("<|Date|>", "5th october 2034"))