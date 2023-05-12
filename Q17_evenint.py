y_list= input("Enter integers").split()
y_int=[ int(num) for num in y_list]
x=list( filter(lambda z: z %2 == 0 ,y_int))
print (x)