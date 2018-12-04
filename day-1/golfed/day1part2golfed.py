t,f=0,{}
while 1:
 for i in[eval(n)for n in open("i")]:
  t+=i
  if f.get(t,0)!=0:print(t);exit()
  f[t]=f.get(t,0)+1