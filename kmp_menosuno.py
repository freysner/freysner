def preKmp(x,m,kmpNext):
   i = 0
   j = -1
   kmpNext[0] = -1
   while (i < m-1):
      while (j > -1  and x[i] != x[j]):
         j = kmpNext[j]
      i+=1
      j+=1
      if (x[i] == x[j]):
         kmpNext[i] = kmpNext[j]
      else:
         kmpNext[i] = j

def KMP(x,y):
   resultado=[]
   n=len(y)
   m=len(x)
   kmpNext=[0]*m
   # Preprocesamiento
   preKmp(x, m, kmpNext)
   #print(kmpNext)
   # Búsqueda
   i = j = 0
   while (j < n):
      while (i > -1 and x[i] != y[j]):
         i = kmpNext[i]
      i+=1
      j+=1
      if (i == m):
         #OUTPUT(j - i)
	 #print("ocurrencia en "+str(j-i))
         resultado.append(str(j-i))
         i = kmpNext[i-1]
   return resultado

