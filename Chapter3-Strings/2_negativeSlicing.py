name = "Pritam"

print(name[-4: -1])  # o/p-> ita
print(name[1:4])     # o/p-> rit
print(name[-5: -1])  # o/p-> rita
print(name[1:5])     # o/p-> rita

print(name[:6])     # o/p-> Pritam
print(name[0:6])    # o/p-> Pritam
print(name[0:])    # o/p-> Pritam
print(name[1:])     # o/p-> ritam
print(name[1:6])    # o/p-> ritam


#Slicing with skip value
word = "abcdefghijkmnopqrs"
print(word[1:6:2]) #o/p-> bdf