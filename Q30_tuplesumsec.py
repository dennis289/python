def tuple_sum(my_tuple):
   t=0
   for tuple in my_tuple:
      if tuple[1] %2 == 0:
        t += tuple[0]
my_tuple=input("Enter a list of tuples")
print(tuple_sum(my_tuple))
