def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def cipherText(text, key):
    result = []
    for i in range(len(text)):
        if text[i].islower():
            x = (ord(text[i]) + ord(key[i]) - ord('a')) % 26
            x += ord('a')
        else:
            x = (ord(text[i]) + ord(key[i]) - ord('A')) % 26
            x += ord('A')
        result.append(chr(x))
    return("" . join(result))

def originalText(text, key):
    result = []
    for i in range(len(text)):
        if text[i].islower():
            x = (ord(text[i]) - ord(key[i]) - ord('a')) % 26
            x += ord('a')
        else:
            x = (ord(text[i]) - ord(key[i]) - ord('A')) % 26
            x += ord('A')
        result.append(chr(x))
    return("" . join(result))
    
key = generateKey('hellomyfriends','friends')
chiper = cipherText('hellomyfriends', key)
print(originalText(chiper,key))
