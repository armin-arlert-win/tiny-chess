import json,os
from urllib.request import Request,urlopen
H=os.getenv("MAKEFUN_ENV_URL")
P=lambda p,b:json.load(urlopen(Request(H+p,data=json.dumps(b).encode())))
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17)
B=(15,17,-15,-17);R=(1,-1,16,-16)
D=(0,0,KN,B,R,B+R,KG);N=(0,0,1,7,7,7,1)
CR={0:2,7:1,112:8,119:4}
V=(0,100,320,330,500,900,0)
TT={};ND=0
K=("&-%.=F5DDU1A>G-E(D","PVZRYQ^L`YY>LDVG]AA8D/G6",",<.6%IIP8BBH&%%RRY","?N`WVMN?]H^>>0WN02","+;%./?(/').7&'>F5D#$'<DS<TSD","`WUMPAVGTDWNN2^BBJJ:2990:220")
class X(Exception):pass
def E(Y):
 v=0
 for i,p in enumerate(Y[0]):
  if p:
   a=abs(p);f=i&7;r=i>>4
   if p<0:r=7-r
   c=6-abs(f-3)-abs(r-3);v+=(p//a)*(V[a]+(4*r+2*c,6*c,4*c,2*c,2*c,-2*c)[a-1])
 return v if Y[1]>0 else -v
def F(e):
 w=e.split();b=[0]*128;i=0
 for c in w[0].replace('/',''):
  if c.isdigit():i+=int(c)
  else:q=(7-i//8)*16+i%8;p='PNBRQK'.index(c.upper())+1;b[q]=p if c<'a' else -p;i+=1
 d=1 if w[1]=='w' else -1;c=sum(1<<'KQkq'.index(x) for x in w[2] if x in'KQkq')
 return [b,d,c,-1,b.index(6),b.index(-6)]
def A(b,s,y):
 for ds,v in(((-15*y,-17*y),1),(KN,2),(KG,6)):
  for d in ds:
   q=s+d
   if not q&136 and b[q]==y*v:return 1
 for ds,v in((R,4),(B,3)):
  for d in ds:
   q=s+d
   while not q&136:
    if b[q]:
     if b[q] in(y*v,y*5):return 1
     break
    q+=d
 return 0
def J(ms,f,q,pr):
 ms+=[f|(q<<7)|(r<<14) for r in(1,4)] if (q>>4)==pr else [f|(q<<7)]
def M(Y,m):
 b,d,c,e,W,K=Y;f=m&127;q=(m>>7)&127;r=(m>>14)&7;p=b[f];a=abs(p);g=d
 B=b[:];c2=c;W2=W;K2=K;B[f]=0;k=B[q]
 if k:c2&=~CR.get(q,0)
 if r:B[q]=g*(0,5,4,3,2)[r]
 else:
  B[q]=p
  if a==6:
   if g>0:W2=q;c2&=~3
   else:K2=q;c2&=~12
   if abs(q-f)==2:u=f+3 if q>f else f-4;v=q-1 if q>f else q+1;B[u]=0;B[v]=g*4
  elif a==4:c2&=~CR.get(f,0)
 return [B,-g,c2,-1,W2,K2]
def G(Y):
 b,d,c=Y[0],Y[1],Y[2];ms=[];v=16*d;sr=1+5*(d<0);pr=7*(d>0)
 for f,p in enumerate(b):
  if p*d<=0:continue
  a=abs(p)
  if a==1:
   q=f+v
   if b[q]==0:
    J(ms,f,q,pr)
    if (f>>4)==sr and b[f+2*v]==0:ms.append(f|((f+2*v)<<7))
   for dt in(v-1,v+1):
    q=f+dt
    if q&136:continue
    if b[q]*d<0:J(ms,f,q,pr)
  elif a>1:
   ds,n=D[a],N[a]
   for dt in ds:
    q=f+dt;z=n
    while z and not q&136 and b[q]==0:ms.append(f|(q<<7));q+=dt;z-=1
    if z and not q&136 and b[q]*d<0:ms.append(f|(q<<7))
   if a==6:
    k=4 if d>0 else 116
    for w,bb,rk in((1,1 if d>0 else 4,3),(-1,2 if d>0 else 8,4)):
     if c&bb and b[k+w]==0 and b[k+2*w]==0 and b[k+rk*w]==4*d and (w>0 or b[k+3*w]==0) and not any(A(b,k+i*w,-d) for i in(0,1,2)):ms.append(k|((k+2*w)<<7))
 return [m for m in ms if not A((Z:=M(Y,m))[0],Z[4+(d<0)],-d)]
def Z(x):return chr(97+(x&7))+str((x>>4)+1)
def U(m):return Z(m&127)+Z((m>>7)&127)+('qrbn'[(m>>14)-1] if m>>14 else '')
def O(Y,ms,tm=0):return sorted(ms,key=lambda m:10**9 if m==tm else 10000+V[abs(Y[0][(m>>7)&127])] if Y[0][(m>>7)&127] else 0,reverse=True)
def S(Y,d,al,be):
 global ND;ND+=1
 if ND>=25000:raise X
 if d<=0:
  st=E(Y)
  if st>=be:return be
  if st>al:al=st
 ms=[m for m in G(Y) if d>0 or Y[0][(m>>7)&127] or m>>14]
 if d>0:
  k=tuple(Y[0]);tm=TT.get(k,0)
  if not ms:return -99999 if A(Y[0],Y[4+(Y[1]<0)],-Y[1]) else 0
 else:tm=0;k=0
 bm=0
 for m in O(Y,ms,tm):
  if (sc:=-S(M(Y,m),d-1 if d>0 else 0,-be,-al))>al:al=sc;bm=m
  if al>=be:break
 if d>0:TT[k]=bm
 return al
def C(fe,lg,gn,pl):
 global ND,TT;i=(pl-8-(gn%2==0))//2
 if 1<=gn<=6 and 0<=i:
  s=K[gn-1]
  if 2*i+1<len(s):
   a=ord(s[2*i])-35;b=ord(s[2*i+1])-35;m=Z(((a>>3)<<4)|(a&7))+Z(((b>>3)<<4)|(b&7))
   if m in lg:return m
 Y=F(fe);ND=0;TT={};lm=[m for m in G(Y) if U(m) in lg]
 if not lm:return lg[0]
 bm=lm[0];al=-10**9
 for d in range(1,12):
  try:
   for m in O(Y,lm):
    if (sc:=-S(M(Y,m),d-1,-10**9,-al))>al:al=sc;bm=m
  except X:break
 return U(bm)
if __name__=="__main__":
 g=P("/game",{})
 while g["status"]!="done":g=P("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"],g["game"],g["plies"])}) if g["status"]=="your_move" else P("/game",{})
