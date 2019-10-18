"""
andresvallejoz1991
"""
#listado con las notas y la calificacion cualitativa
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
#Funcion lambda con la condicional
resultado = filter(lambda x: x[3]=="Regular" or x[3]=="Bueno", notas)
#El condicioanl filtra las notas cualitativas de Regular o Bueno.
print(list(resultado))#Impresion de resultados.





