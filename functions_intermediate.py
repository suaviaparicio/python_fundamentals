# 1. Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


# 1.1. Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# 1.2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

# 1.3. En el directorio_deportes, cambia "Messi" por "Andrés".
# 1.4. Cambia el valor 20 en z a 30.


# 2. Iterar a través de una lista de diccionarios:
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
# Por ejemplo, dada la siguiente lista:
# estudiantes = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
