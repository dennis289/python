number_list=input ("Enter integers").split()
number_int= [int(num) for num in number_list]
x= list(filter(lambda y: y %2 == 0 , number_int))
sum=sum(x)
print(sum)
