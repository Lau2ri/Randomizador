import matplotlib.pyplot as plt
import time

_semilla = int(time.time_ns())

# Función para generar números entre 1 y 5
def random_5():
    global _semilla
    # Generador congruencial lineal (LCG)
    _semilla = (_semilla * 1103515245 + 12345) & 0x7fffffff
    return (_semilla % 5) + 1

# Función recursiva para generar números entre 1 y 7
def random_7():
    num = (random_5() - 1) * 5 + random_5()
    if num <= 21:
        return ((num - 1) % 7) + 1
    return random_7()

# Aquí se utiliza random_7 para generar 500 números aleatorios
resultados = []
for i in range(5000):
    resultados.append(random_7())

# Aquí se grafican estos número en un histograma
plt.hist(resultados, bins=7, edgecolor='black', rwidth=0.8)
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.title('Distribución de números aleatorios entre 1 y 7 de 5000 muestras')
plt.xticks(range(1, 8))
plt.savefig('histograma.png', dpi=300, bbox_inches='tight')
print("FRECUENCIA DE LOS NÚMEROS:")
for i in range(1, 8):
    freq = resultados.count(i)
    print(f"Número {i}: {freq} veces ({freq/50:.1f}%)")

plt.show()