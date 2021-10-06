
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i]) - ord('a')) % 26
        x += ord('a')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) - ord('a')) % 26
        x += ord('a')
        orig_text.append(chr(x))
    return("" . join(orig_text))
    
key = generateKey('hellomyfriends','friends')
chiper = cipherText('hellomyfriends', key)
print(originalText(chiper,key))