x=input("Enter numbers").split()
x.sort(key=lambda x:len(str(x)))
print(x)