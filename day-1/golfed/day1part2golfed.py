t,f=0,{}
while 1:
 for i in open("i"):
  t+=int(i)
  if f.get(t,0):print(t);exit()
  f[t]=1