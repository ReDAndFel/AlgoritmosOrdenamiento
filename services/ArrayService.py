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

def exec():
    data = {}

    for i in range(2):
        n=1000  
        size = pow(n, i+1)
        case_name = f"caso{i+1}"
        array = generar_array(size)
        data[case_name] = {"array": array}

    with open(json_matrix_file_path, 'w') as file_json:
        json.dump(data, file_json)
