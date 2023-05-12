x=["hello","fellow","yellow"]
def long_sfx(strg_list):
    suffix=strg_list[0]
    for string in strg_list[1:]:
        min_lth=min(len(suffix),len(string))
        i=0
        while i<min_lth and suffix[-1-i] == string[-1-i]:
            i+=1
            suffix=suffix[-i:]
        return suffix
print(long_sfx(x))