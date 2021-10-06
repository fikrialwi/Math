def encryptCC(txt,n):
    p = ""
    for i in txt:
        if i == " ":
            p+=" "
        p += chr((ord(i)-97+n)%26+97)
    return p    
def decryptCC(txt,n):
    p = ""
    for i in txt:
        if i == " ":
            p+=" "
        p += chr((ord(i)-97-n)%26+97) 
    return p
print(encryptCC("halo nama saya dzulfikri",6))
for i in range(0,27):
    print(decryptCC("ymnmdbgnswgk",i),"-",i)
