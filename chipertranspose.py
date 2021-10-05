import numpy as np
def encryptTranspose(txt,key):
    result = ""
    length = len(txt)
    while length % key > 0:
        txt += "x"
    length = len(txt)
    n = length//key
    for i in range(key):
        for j in range (n):
            result = result+text[i+j*k]
    return result
def decryptTranspose(txt,key):
    [key,n] = [len(txt)//key, len(txt)//key]
    result = ""
    for i in range(key):
        for j in range (n):
            result = result+text[i+j*k]
    return result
    
    
print(encryptTranspose("Hallo saya dari mana",6))    
    