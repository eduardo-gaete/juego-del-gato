# Ruta del archivo de entrada
ruta_archivo = 'archivo_entrada.txt'
# Ruta del archivo de salida
ruta_resumen = 'resumen.txt'

# Inicializamos los contadores
contador_letras = 0
contador_espacios = 0

# Abrimos el archivo en modo lectura
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    # Leemos el contenido del archivo
    contenido = archivo.read()
    
    # Recorremos cada caracter en el contenido del archivo
    for caracter in contenido:
        if caracter.isalpha():
            contador_letras += 1
        elif caracter.isspace():
            contador_espacios += 1

# Abrimos el archivo en modo escritura
with open(ruta_resumen, 'w', encoding='utf-8') as archivo_resumen:
    # Escribimos el resumen en el archivo
    archivo_resumen.write(f"Cantidad de letras: {contador_letras}\n")
    archivo_resumen.write(f"Cantidad de espacios: {contador_espacios}\n")