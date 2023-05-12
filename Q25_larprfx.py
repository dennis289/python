x=["floor","flour","florence"]
def lar_prfx(strg):
    prefix = strg[0]
    for string in strg:
        while string.find(prefix) !=0:
            prefix=prefix[:-1]
    return prefix
print(lar_prfx(x))

