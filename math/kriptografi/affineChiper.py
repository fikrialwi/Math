def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 
def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None # modular inverse does not exist 
  else: 
    return x % m

def affineEncrypt(text,key):
  text = text.replace(' ','')
  result = ''
  for i in text:
    a = ord('a')
    if i.isupper():
      a = ord('A')
    x = (key[0]*(ord(i)-a) + key[1])%26
    x += a
    result += chr(x)
  return result
def affineDecrypt(text,key):
  result = ''
  for i in text:
    a = ord('a')
    if i.isupper():
      a = ord('A')
    x = (modinv(key[0],26)*(ord(i)-a) - key[1] )%26
    x += a
    result += chr(x)
  return result

enc = affineEncrypt('hello world',[5,5])
print(enc)
print(affineDecrypt(enc,[5,5]))
print(modinv(5,26))
print(ord('o'))