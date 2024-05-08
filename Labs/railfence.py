def rail(s,d=2):
  r=checkr=c=pr=count=0
  end=len(s)
  enc=""
  for f in range(0,d):
   for i in range(count,end):
    if checkr==r:
      enc=enc + s[i]
    if r==d-1 or (r!=0 and r<pr):
      pr=r
      r-=1  
      c+=1  
    else:
      if r!=0 and c!=0:
        pr+=1
      elif r==0 and c!=0:
        pr-=1
      r+=1 
      c+=1
   checkr+=1
   pr=checkr-1
   count+=1
   r=c=checkr
  print("Encrypted Text is:",enc)
  print("Decrypted Text is:",s)
  
      
rail("Pakistan",2)