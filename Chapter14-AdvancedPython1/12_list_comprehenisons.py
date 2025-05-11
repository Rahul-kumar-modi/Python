# Printing the square of elements from the list.

l = [1,2,4,3,7]

# 1st way->
# squareList = []
# for item in l:
#     squareList.append(item*item)

#2nd way->
squareList = [i*i for i in l]
print(squareList)