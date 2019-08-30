import numpy as np

x=np.array([6,3,5,2,1,4,9,7,8])
y=np.array([2,1,3,5,3,9,8,10,7])


sortId=np.argsort(x)
x=x[sortId]
y=y[sortId]
minm = np.array([])
maxm = np.array([])
i = 0
while i < y.size-1:
   while(y[i+1] >= y[i]):
      i+=1

   maxm=np.insert(maxm,0,i)
   i+=1
   while(y[i+1] <= y[i]):
      i+=1

   minm=np.insert(minm,0,i)
   i+=1

print minm, maxm
