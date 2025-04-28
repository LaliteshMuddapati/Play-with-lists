L=[4,5,1,2,9,7,10,8]
print("Original list: ", L)

count=0

for i in L:
    count =+ i

avg=count/len(L)

print("Sum= ", count)
print("Average= ", avg)

L.sort()
print(L)

print("The smallest element is: ", L[0])
print("The largets element is: ", L[-1])
