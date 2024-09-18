from Funciones import nuevo_Tema, nuevo_subtema


print('hola mundo')
print('saludos')
numero = 5
print(numero)



def error():
    dhgeuirhgsrgkergwaykrgbauwyr

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
numero = 5
print ("factorial de ", numero, " es ", factorial(numero))

nuevo_Tema("variables")
edad = 20
print("edad:", edad)

altura = 1.65
print("altura:", altura)

nombre = "Eduardo"
print("nombre:" , nombre)

es_trabajador = True
print("es_trabajador:" , es_trabajador)

nuevo_Tema("listas")
frutas = ['manzanas', 'peras', 'piñas', 'naranjas' , 'guayabas' , 'papayas']
print('frutas:', frutas)

varias_cosas = ['Escuela', 23, True, frutas]
print('varias_cosas') 

"""
   Seleccionando un elemento
   Comentario en multiples lineas 
"""
print('frutas[4]: ', frutas[4])
print('frutas[-2]: ', frutas[-2])

print('frutas[1:5]:', frutas[1:5])
print('frutas[1:5:2]:', frutas[1:5:2])

# Agregando un elemento
frutas.append('fresas')
print("frutas: ", frutas)
# Quitando un elemento
frutas.remove('naranjas')
print("frutas; ", frutas)
# Insertando un elemento en la posicion descrita
frutas.insert(4, 'kiwi')
print("frutas; ", frutas)

# Creando una lista vacia
calificaciones = []
print("calificaciones", calificaciones)
libros = []
print("libros:" , libros) 

frutas.reverse()
print("frutas: ", frutas)
frutas.sort()
print("frutas: ", frutas)

nuevo_Tema("diccionarios")

persona ={"nombre": "Pedro", 
          "apeliido": "Pérez", 
          "edad": 48, 
          "estatura": 1.70, 
          "hijos": ["Casimira", "Bryan", "Eliud"]}

print('persona: ', persona)

print("persona.keys(): ", persona.keys())
print("persona.values(): ", persona.values())

print('persona.get("nombre"):', persona.get("nombre"))
print('persona.get("estatura"):', persona.get("estatura"))

print("persona.items(): ", persona.items())

nuevo_Tema("Ciclos")
nuevo_subtema("for")
for i in range(10):
    print(i) 

print("######")
for i in range (3,10):
    print(i)

print("######")
for i in range (3,10,2):
    print(i)

print("len(frutas):" , len(frutas))

for fruta in frutas:
    print(fruta)

print("###### con len")
for indice in range(len(frutas)):
    print("Indice ", indice , frutas[indice])

print("####### con enumerate")
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

print("####### for en un diccionario")
for key, value in persona.items():
    print(key, value)   