def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))  


def encryptVigenereChiper(text, key):
    if text.isalnum() == False:
        return "Sorry my Boy, I can't excute your code"
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


def decryptVignereChiper(text, key):
    if text == "Sorry my Boy, I can't excute your code" or text.isalnum() == False:
        return ":("
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