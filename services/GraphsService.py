import JsonService as js
import matplotlib.pyplot as plt
import numpy as np

json_times_file_path = "./times2.json"
data = js.read_json(json_times_file_path)

labels = list(data.keys())
values = list(data.values())

# Asegurarse de que todas las listas tengan el mismo tamaño
min_length = len(labels)
labels = labels[:min_length]
values = values[:min_length]

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(min_length)
width = 0.4

ax.bar(x - width/2, values, width)

ax.set_xlabel('Algoritmo')
ax.set_ylabel('Tiempo en segundos')
ax.set_title('Comparación de tiempos algoritmos de ordenamiento')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()