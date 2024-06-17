# Ruta del archivo de entrada
ruta_archivo = 'archivo.txt'
# Ruta del archivo de salida
ruta_resumen = 'resumen.txt'

# Inicializamos los contadores
contador_letras = 0
contador_espacios = 0

# Abrimos el archivo en modo lectura
with open(ruta_archivo, 'r', encoding='utf-8') as archivo: # utf-8 se utiliza para asegurar que el texto se lea y escriba correctamente, especialmente si hay caracteres especiales o no latinos en el archivo.
    # Leemos el contenido del archivo
    contenido = archivo.read()
    
    # Recorremos cada caracter en el contenido del archivo
    for caracter in contenido:
        if caracter.isalpha():  # caracter.isalpha() se utiliza para contar cuántos caracteres en el archivo son letras del alfabeto. 
            contador_letras += 1
        elif caracter.isspace(): # caracter.isalpha() se utiliza para contar cuántos espacios en blanco hay en el archivo. 
            contador_espacios += 1

# Abrimos el archivo en modo escritura
with open(ruta_resumen, 'w', encoding='utf-8') as archivo_resumen:
    # Escribimos el resumen en el archivo
    archivo_resumen.write(f"Cantidad de letras: {contador_letras}\n") #  write se utiliza para escribir texto en un archivo.
    archivo_resumen.write(f"Cantidad de espacios: {contador_espacios}\n") # la "n" es un salto de linea en el archivo de texto.
