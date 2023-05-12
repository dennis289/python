x=input("Enter a string ")
my_dict={}
for char in x:
    if char in my_dict:
        my_dict[char] +=1
    else:
        my_dict[char]=1    
max_char=max(my_dict,key=my_dict.get)
print(str(max_char))
