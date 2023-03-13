#1-Seleccionar de lista de valores los pares  ejemplo tarea 2
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)
#[2, 4, 6, 8]

#usando filter para eliminar pares se reliza con funcional
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print(pares)
[2, 4, 6, 8]


#2- Eliminar los repetidos de una lista ejemplo tarea 2 ejercicio 6
test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]

def eliminar_reps(list):
    res = []
    for item in list:
        if item not in res:
            res.append(item)
    return res

print(eliminar_reps([]))
print(eliminar_reps([3,3,3,3,3,3,3]))

#usando filter para eliminar repetidos

test_list = [1,1,2,2,3,3,3,3,3,4,5,6,6,7,7]
pares = list(filter(lambda x:x==test_list ,test_list)) #este no mefunciona no supe como creal la logica del igual
print(test_list)
[2, 4, 6, 8]



# 3-elevar al cubo una liata ejercicio de la tarea 2 ejercicio 4
def elevar_al_cubo(lista):
    res = []
    for item in lista:
        res.append(item ** 3)
    return res

#Elevar al cubo con funcion lambda
def Cubo(x):
     return x ** 3
 
Cubo = lambda x: x ** 3
print(Cubo(3))
27
print(Cubo(5))

# elevar al cubo usando funcion map donde ingresa una lista de valores y devuelve a cubo
enteros = [1, 2, 4, 7]
cubos = list(map(lambda x : x ** 3, enteros))
print(cubos)
[1, 4, 16, 49]

#4 Strings intercaladas ejercicio tarea

def intercalar_strings(str1, str2):
    if len(str1) != len(str2):
        return "Las strings deben ser del mismo largo"
    res = ""
    for i in range(0, len(str1)):
        res += str1[i] + str2[i]
    return res
# str1 = input("Ingrese la primera palabra \n")
# str2 = input("Ingrese la segunda palabra \n")
# print(intercalar_strings(str1, str2))

#para hacer la iteracion con funcion,se ingresan los valores y me imprime los valores iterados
str1=["melania"]
str2=["herrera"]
str1 = list(map(lambda x:x[::-1],str1))
str2 = list(map(lambda x:x[::-1],str2))
print(str1)
print(str2)



