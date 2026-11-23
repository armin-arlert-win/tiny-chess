import json,os
from urllib.request import Request,urlopen
U=os.getenv("MAKEFUN_ENV_URL") or os._exit(1)
def P(p,b):
 q=Request(U+p,data=json.dumps(b).encode())
 try:
  with urlopen(q) as r:return json.load(r)
 except:os._exit(1)
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33)
KG=(-17,-16,-15,-1,1,15,16,17)
B=(15,17,-15,-17);R=(1,-1,16,-16)
W={2:(KN,1),3:(B,7),4:(R,7),5:(B+R,7),6:(KG,1)}
CR={0:2,7:1,112:8,119:4}
ND=0
class X(Exception):pass
def t(p,s):
 f=s&7;r=s>>4
 if p<0:r=7-r
 c=6-abs(f-3)-abs(r-3)
 return ((14*r+2*c,6*c,4*c)+(2*c,)*3)[abs(p)-1]
def E(Y):
 v=sum(p//abs(p)*(V[abs(p)]+t(p,i)) for i,p in enumerate(Y[0]) if p)
 return v if Y[1]>0 else -v
def F(e):
 w=e.split();b=[0]*128
 r=''.join(x if x>'9' else '1'*int(x) for x in w[0] if x!='/')
 for i,c in enumerate(r):
  if c!='1':
   q=(7-i//8)*16+i%8;p='PNBRQK'.index(c.upper())+1
   if c.islower():p=-p
   b[q]=p
 d=1 if w[1]=='w' else -1
 c=('K' in w[2])+2*('Q' in w[2])+4*('k' in w[2])+8*('q' in w[2])
 p=-1 if w[3]=='-' else ord(w[3][0])-97+(int(w[3][1])-1)*16
 return [b,d,c,p,b.index(6),b.index(-6)]
def A(b,s,y):
 for ds,v in(((-15*y,-17*y),1),(KN,2),(KG,6)):
  for d in ds:
   q=s+d
   if not(q&136) and b[q]==y*v:return 1
 for ds,v in((R,4),(B,3)):
  for d in ds:
   q=s+d
   while not(q&136):
    if b[q]:
     if b[q] in(y*v,y*5):return 1
     break
    q+=d
 return 0
def J(ms,f,q,pr):
 if (q>>4)==pr:
  for r in(1,4):ms.append(f|(q<<7)|(r<<14))
 else:ms.append(f|(q<<7))
def M(Y,m):
 b,d,c,e,W,K=Y
 f=m&127;q=(m>>7)&127;r=(m>>14)&7
 p=b[f];a=abs(p);g=d
 B=b[:];c2=c;W2=W;K2=K
 B[f]=0
 k=B[q]
 if a==1 and q==e and not k:
  v=q-16*g;j=B[v];B[v]=0
 elif k:
  c2&=~CR.get(q,0)
 if r:
  w=(0,5,4,3,2)[r];B[q]=g*w
 else:
  B[q]=p
  if a==6:
   if g>0:W2=q;c2&=~3
   else:K2=q;c2&=~12
   if abs(q-f)==2:
    u,v=(f+3,f+1) if q>f else (f-4,f-1);B[u]=0;B[v]=g*4
  elif a==4:c2&=~CR.get(f,0)
 e2=-1
 if a==1 and abs(q-f)==32:e2=f+16*g
 return [B,-g,c2,e2,W2,K2]
def G(Y):
 b,d,c,e=Y[0],Y[1],Y[2],Y[3]
 ms=[]
 for f in range(128):
  if f&136:continue
  p=b[f]
  if p*d<=0:continue
  a=abs(p)
  if a==1:
   v=16*d;sr=1 if d>0 else 6;pr=7 if d>0 else 0
   q=f+v
   if b[q]==0:
    J(ms,f,q,pr)
    if (f>>4)==sr and b[f+2*v]==0:ms.append(f|((f+2*v)<<7))
   for dt in(v-1,v+1):
    q=f+dt
    if q&136:continue
    if b[q]*d<0:J(ms,f,q,pr)
    elif q==e:ms.append(f|(q<<7))
  elif a>1:
   ds,n=W[a]
   for dt in ds:
    q=f+dt;z=n
    while z and not(q&136) and b[q]==0:
     ms.append(f|(q<<7));q+=dt;z-=1
    if z and not(q&136) and b[q]*d<0:ms.append(f|(q<<7))
   if a==6:
    k=4 if d>0 else 116
    for w,bb,rk in((1,1 if d>0 else 4,3),(-1,2 if d>0 else 8,4)):
     if c&bb and b[k+w]==0 and b[k+2*w]==0 and b[k+rk*w]==4*d and (w>0 or b[k+3*w]==0) and not A(b,k,-d) and not A(b,k+w,-d) and not A(b,k+2*w,-d):ms.append(k|((k+2*w)<<7))
 return [m for m in ms if not A((Z:=M(Y,m))[0],Z[4] if d>0 else Z[5],-d)]
def U(m):
 f=m&127;q=(m>>7)&127
 return 'abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[q&7]+str((q>>4)+1)+('qrbn'[(m>>14)-1] if m>>14 else '')
def O(Y,ms):
 def k(m):
  f=m&127;q=(m>>7)&127;c=Y[0][q]
  return 10000+10*V[abs(c)]-V[abs(Y[0][f])] if c else 0
 return sorted(ms,key=k,reverse=True)
def S(Y,d,al,be,pl):
 global ND
 ND+=1
 if ND>=40000:raise X
 if d<=0:
  st=E(Y)
  if st>=be:return be
  if st>al:al=st
  ms=[m for m in G(Y) if Y[0][(m>>7)&127] or m>>14]
  for m in O(Y,ms):
   sc=-S(M(Y,m),0,-be,-al,pl+1)
   if sc>al:al=sc
   if al>=be:return be
  return al
 ms=G(Y)
 if not ms:return -99999+pl if A(Y[0],Y[4] if Y[1]>0 else Y[5],-Y[1]) else 0
 for m in O(Y,ms):
  sc=-S(M(Y,m),d-1,-be,-al,pl+1)
  if sc>al:al=sc
  if al>=be:break
 return al
def C(fe,lg):
 global ND
 Y=F(fe);ND=0
 lm=[m for m in G(Y) if U(m) in lg]
 if not lm:return lg[0]
 bm=lm[0]
 for d in range(1,12):
  try:
   al=-10**9
   for m in O(Y,lm):
    sc=-S(M(Y,m),d-1,-10**9,-al,1)
    if sc>al:al=sc;bm=m
  except X:break
 return U(bm)
if __name__=="__main__":
 g=P("/game",{})
 while g["status"]!="done":
  g=P("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])}) if g["status"]=="your_move" else P("/game",{})
