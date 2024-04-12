import json
import random

# Ruta absoluta para el archivo JSON
json_matrix_file_path = "./array.json"

def generar_array(n):
    array = []
    for _ in range(n):
        numero = random.randint(100000, 999999)  # Generar número aleatorio de 6 dígitos
        array.append(numero)
    return array

def generar_dos_array(n):
    size = pow(2, n) #Crea una tamaño de 2 a la n
    print("Tamaño del array:", size)  # Imprimir el valor del tamaño
    array1 = generar_array(size)
    array2 = generar_array(size)
    return array1, array2

data = {}
for i in range(2):
    n=3+(i+1)
    case_name = f"caso{i+1}"
    array1, array2 = generar_dos_array(n)
    data[case_name] = {"array1": array1, "array2": array2}

with open(json_matrix_file_path, 'w') as file_json:
    json.dump(data, file_json)
