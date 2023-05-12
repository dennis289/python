y=input("Enter a string").split()
vowels='a''e''i''o''u''A''E''I''O''U'
for word in y:
    vow_count=0
    for i in range( 0,len(word)) :
       if word[i] in vowels:
           vow_count += 1
    print (vow_count)