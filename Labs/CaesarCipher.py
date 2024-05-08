d=[chr(i) for i in range(ord("a"),ord("z")+1)]
def caesar_cipher(t,k=3):
 
  ct=""
  pt=""
  
  for txt in t:
 
     cs=txt.lower()
     pos=(d.index(cs)+ k)%26
     ct=ct + d[pos]
     p=pos-k
     pt=pt+ d[p]
     
    
 
  print("Encrypted Text is:",ct)
  print("Decrypted Text is:",pt)
  

caesar_cipher("SyedAbid",3)