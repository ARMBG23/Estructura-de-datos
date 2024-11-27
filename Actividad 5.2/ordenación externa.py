import heapq
import random
import pandas as pd

# Generar datos de ejemplo
def generar_datos(n):
    """Genera una lista de datos de ejemplo."""
    datos = []
    zonas = ["Clientes", "Empleados", "Carga/Descarga", "Discapacitados/Embarazadas", "Express"]
    for i in range(n):
        zona = random.choice(zonas)
        espacio = f"Espacio {random.randint(1, 500)}"
        estado = "Disponible" if random.random() > 0.5 else "Ocupado"
        datos.append((zona, espacio, estado))
    random.shuffle(datos)  # Mezclar los datos para asegurar aleatoriedad
    return datos

# Dividir lista en bloques pequeños y ordenarlos
def dividir_y_ordenar(datos, tam_bloque):
    """Divide la lista en bloques ordenados."""
    bloques = []
    for i in range(0, len(datos), tam_bloque):
        bloque = sorted(datos[i:i + tam_bloque])
        bloques.append(bloque)
    return bloques

# Fusionar bloques ordenados
def fusionar_bloques(bloques):
    """Fusiona múltiples bloques ordenados en una lista final ordenada."""
    heap = [(bloque[0], idx, 0) for idx, bloque in enumerate(bloques) if bloque]
    heapq.heapify(heap)
    resultado = []

    while heap:
        menor, idx, pos = heapq.heappop(heap)
        resultado.append(menor)
        if pos + 1 < len(bloques[idx]):
            heapq.heappush(heap, (bloques[idx][pos + 1], idx, pos + 1))

    return resultado

# Exportar datos a Excel
def exportar_a_excel(datos, archivo_salida):
    """Exporta los datos a un archivo de Excel organizado por zona."""
    df = pd.DataFrame(datos, columns=["Zona", "Espacio", "Estado"])
    df = df.sort_values(by=["Zona", "Espacio"])
    df.to_excel(archivo_salida, index=False)

# Ejecutar ejemplo simple
if __name__ == "__main__":
    num_datos = 1000
    tam_bloque = 100
    archivo_excel = "datos_estacionamiento.xlsx"

    print("Generando datos...")
    datos = generar_datos(num_datos)

    print("Dividiendo y ordenando datos en bloques...")
    bloques = dividir_y_ordenar(datos, tam_bloque)

    print("Fusionando bloques ordenados...")
    datos_ordenados = fusionar_bloques(bloques)

    print("Exportando datos a Excel...")
    exportar_a_excel(datos_ordenados, archivo_excel)

    print("Datos ordenados:")
    for dato in datos_ordenados[:10]:  # Mostrar solo los primeros 10 resultados
        zona, espacio, estado = dato
        print(f"{zona}, {espacio}, {estado}")

    print(f"Datos restantes exportados a {archivo_excel}")
