y=input("Enter a string ")
def most_common_substrg(y):
   my_dict={}
   for string in y:
      for i in range(len(string)-2):
          sub_strg=string[i:i+3]
          if sub_strg in my_dict:
            my_dict[sub_strg] +=1
          else:
            my_dict[sub_strg]=1
   most_apprd=0
   max_subs =None       
   for sub_strg ,count in my_dict.items():
      if count > most_apprd :
       most_apprd= count
       max_subs=sub_strg
       return most_apprd
print(most_common_substrg(y))

