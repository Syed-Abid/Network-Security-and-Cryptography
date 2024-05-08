def match(ma,dia):
 c1=c2=None
 b=0
 enc=""
 r1=r2=None
 length=len(dia)
 co=0
 dec=""
 for d in range(0,len(dia)):
  n1=list(dia[d])
  dec=dec+dia[d]
  c1=c2=r1=r2=None
  for r in range(0,5):
    if n1[b] in ma[r] or n1[b]=="j": #and r<1:
     if n1[b]=="j": #covering j case
       if "i" in ma[r]:
        c1=ma[r].index("i")
        r1=r
     else:
      c1=ma[r].index(n1[b])
      r1=r
    b+=1
    if n1[b] in ma[r] or n1[b]=="j": #and r<1:
     if n1[b]=="j":
       if "i" in ma[r]:
        c2=ma[r].index("i")
        r2=r
     else:
      c2=ma[r].index(n1[b])
      r2=r
    b=0
    if c1==c2 and c1!=None and c2!=None: #if cols are same
      if r1<4:
       enc=enc+ma[r1+1][c1]
      else:
        enc=enc+ma[0][c1]
      if r2<4:
       enc=enc+ma[r2+1][c2]
      else:
        enc=enc+ma[0][c2]
      #print("Encrypted Text is:",enc)
      break
    elif r1==r2 and r1!=None:
      if c1<4:
       enc=enc+ma[r1][c1+1]
      else:
        enc=enc+ma[r1][0]
      if c2<4:
       enc=enc+ma[r2][c2+1]
      else:
        enc=enc+ma[r2][0]
      #print("Encrypted Text is:",enc)
      break
    elif r1!=None and r2!=None and c1!=None and c2!=None and c1<c2:
       nc=(c2-c1)#->
       enc=enc+ma[r1][c1+nc]
       nc=abs(c1-c2) #<-
       enc=enc+ma[r2][c2-nc]
       #print("Encrypted Text is:",enc)
       break
      
    else: #if c1 is greater
       if c1!=None and c2!=None and r1!=None and r2!=None and c1>c2:
        nc=(c1-c2) #<-
        enc=enc+ma[r1][c1-nc]
        nc=abs(c2-c1)#->
        enc=enc+ma[r2][c2+nc]
        #print("Encrypted Text is:",enc)
        break
 
 print("Encrypted Text is:",enc)
 print("Decrypted Text:",dec)    
  
def diagraph(m,t):
  tf=False
  temp=t[0]
  di=[]
  count=0
  temp=te=""
  for txt in t:
   if te!="":
     temp=te
     te=""
   if temp==txt:
     temp=temp+"x"
     te=txt
   else:
     temp=temp + txt
   count+=1
   if len(temp)==2 or count==len(t):
    di.append(temp)
    temp=""
  if (len(di[-1])==1):
    di[-1]=di[-1]+"z"
  match(m,di)
def playfair(txt,key):
 txt=txt.lower()
 key=key.lower()
 alp=[chr(i) for i in range(ord('a'),ord('z')+1)]
 val=[True for i in range(ord('a'),ord('z')+1)]
 count=cr=cc=0
 mat=[]
 for r in range(1,6):
  a=[]
  for c in range(1,6):
    a.append(c)
  mat.append(a)
 for k in key: #populating matrix with key
   cp=alp.index(k)
   if val[cp]!=False: #if not already put in matrix
    mat[cr][cc]=k
    count+=1
    val[cp]=False
    if cc<4:
     cc+=1
    else:
      cc=0
      if cr!=4:
       cr+=1
 for lo in range(26): #now populating matrix
   if val[lo]==True and alp[lo]!="j":
     mat[cr][cc]=alp[lo]
     val[lo]=False
     if cc<4:
      cc+=1
     else: # cc==4
      cc=0
      if cr<4:
       cr+=1
 diagraph(mat,txt)
playfair("I am Abid","monarchy")
