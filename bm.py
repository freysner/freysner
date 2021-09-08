ASIZE=256
def preBmBc(x,m,bmBc):
   vector=[m]*ASIZE
   for i in range( m - 1):
      vector[ord(x[i])] = m - i - 1
   return vector


def suffixes(x,m,suff):
   suff[m - 1] = m
   g = m - 1
   for i in range(m - 2,0, -1):
      if (i > g and suff[i + m - 1 - f] < i - g):
         suff[i] = suff[i + m - 1 - f]
      else:
         if (i < g):
            g = i
         f = i
         while (g >= 0 and x[g] == x[g + m - 1 - f]):
            g-=1
         suff[i] = f - g

def preBmGs(x,m,bmGs):
   suff=[0]*m #m=XSIZE
   suffixes(x, m, suff)
   for i in range(m):
      bmGs[i] = m
   j = 0
   
   for i in range(m - 1,0,-1):
      if (suff[i] == i + 1):
         for j in range(i, m - 1 - i, 1):
            if (bmGs[j] == m):
               bmGs[j] = m - 1 - i
   for i in range(m - 1):
      bmGs[m - 1 - suff[i]] = m - 1 - i
   return bmGs

def BM(x,y):
   resultado=[]
   m=len(x)
   n=len(y)
   bmGs=[m]*m
   bmBc=[m]*ASIZE
   #Preprocessing
   bmGs=preBmGs(x, m, bmGs)
   #print(bmGs)
   bmBc=preBmBc(x, m, bmBc)
   #print(bmBc)
   # Searching
   j = 0
   while (j <= n - m):
      i=m-1
      while(i >= 0 and x[i] == y[i + j]):
         i-=1
      if (i < 0):
	 #OUTPUT(j)
	 #print("Ocurrencia en "+str(j))
         resultado.append(str(j))
         j += bmGs[0]
      else:
         j += max(bmGs[i], bmBc[ord(y[i + j])] - m + 1 + i)
   return resultado
      
