string_list=input("Enter strings separated by spaces").split()
string_list=max(string_list,key=len)
print(string_list)