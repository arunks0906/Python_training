def fibb(num):
    if num<=1:
        return num
    else:
        return fibb(num-1) + fibb(num-2)

num=int(input("Enter a number: "))
if num<=0:
    print("Invalid number")
else:
    for i in range(num):
        print(fibb(i))