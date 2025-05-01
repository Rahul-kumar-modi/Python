#Write a program to find out whether a given post is talking about "rupesh" or not.

post = input("Enter the post: ")

if("rupesh" in post.lower()):
    print("This post is talking about rupesh")

else:
    print("This post is not talking about rupesh")