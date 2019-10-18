"""
andresvallejoz1991
"""

mensaje = "No hay medicina que cure lo que no cura la felicidad"
#Particion de la frase en cada palabra
aux1 = mensaje.split()
aux2 = []
for a in resultado1:
	aux2.append(a)

resultado = filter(lambda x: len(x)==2 or len(x)==3, aux2)#Funcion lambda con los condicional
#El condicioanl filtra los pronombres con un numero par de letras.
print(list(resultado))#Impresion de resultados.

		
