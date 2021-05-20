def empKMP(text,pat):
#{ on-line linear version of KMP search } 
	j,k=0,0 
	m=len(text)
	n=len(pat)
	s_Borde=[0]*m
	computarBorde(m,pat,s_Borde)
	cont=0
	while k<n:
		while  j<m  and  pat[j+1]==text[k]: 
			j=j+1
			if  j==m:
				cont=cont+1
			k=k+1
		if  s_Borde[j]==-1:  
			k=k+1 
			j= 0
		else: 
			j=  s_Borde[j]
	print(cont)

def computarBorde(m,pat,s_Bord):
	s_Bord[0] = -1 
	t  = -1
	for  j in range(1, m-2):
		while  0<=t and  pat[t+1]!=pat[j]: 
			s_Bord[t]=t
		t = t+1
		print(j)
		if  pat[t+1]!=pat[j+1]:
			s_Bord[j] =  t 
		else:
			s_Bord[j] =  s_Bord[t] 
	s_Bord[m] =  t; 

cad="ababbbbac"
p="aba"
empKMP(cad,p)
