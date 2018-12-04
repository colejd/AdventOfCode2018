from collections import*
t,f=0,defaultdict(int)
while 1:
 for i in[eval(n)for n in open("i")]:
  t+=i
  if f[t]!=0:print(t);exit()
  f[t]+=1