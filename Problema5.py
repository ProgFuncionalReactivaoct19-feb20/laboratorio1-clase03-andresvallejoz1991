"""
andresvallejoz1991
"""
#Funcion
def blacked(a):
	#Listado
	blakedned = [10, 14, 30, 32, 40, 16]
	if a in blakedned:#Condicional
		return False#Retorna Falso o Verdadero
	else:
		return True

datos = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

resultado = filter(blacked, datos)#Filtar los datos
print(list(resultado))	#Impresion 
