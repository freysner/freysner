import re
cadena = open('NC_AE009949_converted.fasta').read()
#patron = "(((GG(A|C|G)))|(TT(T|C))){2,}"
patron = re.compile("[ACTG]{50}")
print(patron)
x = re.findall(patron, cadena)
print("Se han encontrado " + str(len(x)) + " repeticiones")
#longitud=len(patron)
m=patron.search(cadena)  # match
#print (patron.patron) # None
print(m.group(0))
#print(m.group(1))
##print(len(m.groups()))

#regexes = [
 #   re.compile(p)
  #  for p in ['this', 'that']
#]
#text = 'Does this text match the pattern?'

#print('Text: {!r}\n'.format(text))

#for regex in regexes:
 #   print('Seeking "{}" ->'.format(regex.pattern),
  #        end=' ')

   # if regex.search(text):
    #    print('match!')
    #else:
     #   print('no match')



