def KMPSearch(pat, txt):
	resultado=[]
	M = len(pat)
	N = len(txt)

	#  crear lps[] para guardar el tamaño de los prefijos(saltos)
	lps = [0]*M
	j = 0 # indice para pat[]

	# calcular la tabla lps[]
	computeLPSArray(pat, M, lps)
	#print(lps)
    
	i = 0 # indice para txt[]
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1
		if j == M:
			#print ("Ocurrencia de patrón en posición " + str(i-j))
			resultado.append(str(i-j))
			j = lps[j-1]
		# fallo después de j emparejamientos
		elif i < N and pat[j] != txt[i]:
			# No existe emparejamiento en los lps[0..lps[j-1]] caracteres
			# pero podrían emparejar en los anteriores
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
	return resultado

def computeLPSArray(pat, M, lps):
	len = 0 # longitud previa de prefijo y sufijo

	lps[0] # lps[0] es siempre 0
	i = 1

	# en el bucle se calcula lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# Caso delicado. Considerar el sgte ejemplo.
			# AAACAAAA y i = 7. La idea es similar a
			# la búsqueda paso a paso (fuerza bruta)
			if len != 0:
				len = lps[len-1]

				# Además, notemos que no incrementa i aquí
			else:
				lps[i] = 0
				i += 1

