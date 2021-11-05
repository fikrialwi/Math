def encryptTranspose(txt,key):
    result = ""
    length = len(txt)
    while length % key > 0:
        txt += "x"
        length = len(txt)
    n = length//key
    for i in range(n):
        for j in range (key):
            result += txt[i+j*key]
    return result
def decryptTranspose(txt,key):
    n = len(txt)//key
    result = ""
    for i in range(key):
        for j in range (n):
            result += txt[i+j*key]
    return result
    
f = "z abnerae ssaanaaharlpdtbiafjimaamaa abneaae ss anaahhrlpdt iafjiu" 
d = "zraabm aariaaenlaab apfmnsadjaeshtiaa h unre oxnia kagojkgx sdaensparrx"


for i in range(2,72):
    print(f'{i}-decrypt = {decryptTranspose(d,i)}')