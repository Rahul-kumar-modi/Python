# Write a program to read the text from a given file 'lyrics.txt' and find out whether it contains the word 'Wajood'

f = open("lyrics.txt")
content = f.read()

if("Wajood" in content):
    print("The word Wajood is present in the content")

else:
    print("The word Wajood is not present in the content")

f.close()