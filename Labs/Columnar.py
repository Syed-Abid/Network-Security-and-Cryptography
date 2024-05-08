from math import ceil
def col_cipher(txt,key):
  txt.lower()
  key.lower()
  d=[]
  for i,v in enumerate(key):
     d.append(f"{v}{i}")
  sort=sorted(d)
  ar=[]
  kl=len(key)
  tl=len(txt)
  r=[]
  for i in range(0,kl): #populating matrix with key
    if key[i]==" ":
      r.append("_")
    else:
      r.append(key[i])
    if len(r)==kl or (i==kl-1 and len(r)!=0):
      if len(r)==kl:
        ar.append(r)
        r=[]
      else:
        r.append(key[i])
        ar.append(r)  
  tr=(ceil(tl/kl))+1 #maximum rows
  mbox=tr*kl
  remv=mbox-(tl+kl)
  dec=txt
  r=[]
  for i in range(0,len(txt)): #text is also populated
    if txt[i]==" ":
      r.append("_")
    else:
      r.append(txt[i])
    if len(r)==kl or (i==tl-1 and len(r)!=0):
      if len(r)==kl:
        ar.append(r)
        r=[]
      elif i==tl-1 and len(r)!=0:
        for u in range(0,remv):
          r.append("_")
        ar.append(r)
  enc=""
  n=[]
  for string in sort:
    num = ''.join(filter(str.isdigit, string))
    num=int(num)
    for r in range(1,tr):
      enc=enc+ar[r][num]
  print("Encrypted Text is:",enc)
  print("Decrypted Text is:",dec)
col_cipher("MY NAME IS ABID","hack")