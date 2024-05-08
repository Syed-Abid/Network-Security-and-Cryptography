def vigcipher(t,k):
  p=len(t)
  w=co=0
  enc=""
  dec=" "
  a=[chr(i) for i in range(ord('a'),ord('z')+1)]
  if len(k)< len(t):
    while len(k)!=len(t):
      if co==len(k):
        co=0
      k=k+k[co]
      if len(k)==len(t):
        break
      co=co+1
  while w!=p:
    asc=(a.index(t[w]) + a.index(k[w]))%26
    enc=enc + a[asc]
    w=w+1
  print("encrypt:",enc)
  w=0
  while w!=p:
    dsc=((ord(enc[w])-ord(k[w]))+26%26)
    dec=dec+a[dsc]
    w=w+1
  print("decrypt:",dec)
vigcipher("syed","abid")
