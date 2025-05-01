l1 = "Make a lot of money"
l2 = "buy now"
l3 = "subscribe this"
l4 = "click this"

message = input("Enter your comment: ")

if((l1 in message) or (l2 in message) or (l3 in message) or (l4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")