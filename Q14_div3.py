y=input("Enter numbers").split()
x=[int(num)for num in y]
x=list(filter( lambda a: a % 3== 0 , x))
sum = sum(x)
print(sum)