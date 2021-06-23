def rabinKarp(pat,cad):
    n=len(cad)
    m=len(pat)
    resultado=[]
    contador=0
    if (n>0 and m>0):    # verificar si la cadena esta vacia
        c,p = 0,0        # c = hash de cadena, p = hash de pa
        pm = 256           # nro de caracteres del alfabeto
        q = 33554393     #101# numero primo 
	#q=19
        h = 1            # h multiplicador
        for _ in range(m-1):
            h = (h * pm) % q
        for i in range(m):
            c = (pm * c + ord(cad[i])) % q
            p = (pm * p + ord(pat[i])) % q
        for i in range (n-m+1):
            if (c == p):  # comparando hash de cadena y patron
               	for j in range(m):
            	    if(cad[i+j] != pat[j]):
                        break
                if(j==m-1):
                    resultado.append(str(i))
            if i<n-m:
                c = (pm * (c - h * ord(cad[i])) + ord(cad[i+m])) % q
                if c<0:
                    c=c+q
    return resultado   
