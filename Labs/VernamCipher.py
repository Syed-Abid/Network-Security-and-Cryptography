def vernam_cipher(txt,ky):
  txt=txt.lower()
  ky=ky.lower()
  p=len(txt)
  w=co=0
  enc=""
  dec=" "
  rem=[]
  a=[chr(i) for i in range(ord('a'),ord('z')+1)]
  if len(ky)< len(txt):
    while len(ky)!=len(txt):
      if co==len(ky):
        co=0
      ky=ky+ky[co]
      if len(ky)==len(txt):
        break
      co=co+1
  while w!=p: #computing cipher text
    asc=(int(bin(a.index(txt[w])),2)^int(bin(a.index(ky[w])),2))%26
    rem.append(int(bin(a.index(txt[w])),2)^int(bin(a.index(ky[w])),2))
    enc=enc + a[asc]
    w=w+1
  print("Encrypted Text:",enc)
  w=0
  while w!=p:
    dsc=(int(bin(rem[w]),2)^int(bin(a.index(ky[w])),2))
    dec=dec+a[dsc]
    w=w+1
  print("Decrypted Text:",dec)
vernam_cipher("syedabid","finalyear")
