y_str=input("Enter a string ")
A= '*'
vow='aeiouAEIOU'
trans=str.maketrans(vow,A*len(vow))
y_str=y_str.translate(trans)
print(y_str)