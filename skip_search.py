ASIZE=256

def ArrayCmp(a,aIdx,b,bIdx,Length):
   i = 0
   while(i < Length and aIdx + i < len(a) and bIdx + i < len(b)):
      if (a[aIdx + i] != b[bIdx + i]):
         return 1
      i+=1
   if (i== Length):
      return 0
   else:
      return 1


def SKIP(x,y):
   resultado=[]
   m=len(x)
   n=len(y)
   z=[]
   for i in range(ASIZE):
      z.append([])
   # Preprocessing
   for i in range(m):
      z[ord(x[i])].append(i)
   #Searching

   #print(z)
   for i in range(m-1,n,m):
      ptr=z[ord(y[i])]
      #print(i)
      #print(ptr)
      for j in range(len(ptr)):
         if (ArrayCmp(x,0,y,i-ptr[j],m)==0):
            #print('Ocurrencia en %d\n' % (i-ptr[j]))
            resultado.append(i-ptr[j])
   return resultado

