import string

alfabeto = string.ascii_uppercase 
cantidad_letras = len(alfabeto)

# Frecuencia de las letras más comunes en castellano
frequencias = {"E": 0.1307, "A": 0.1152, "O": 0.0868, "S": 0.0734}

#Calcular la frecuencias de las letras en un texto

def calcular_frecuencias(texto):
    frecuencias = {letra: 0 for letra in alfabeto}
    for char in texto.upper():
        if char in alfabeto:
            frecuencias[char] = frecuencias[char] + 1
    total = sum(frecuencias.values())
    for letra in frecuencias:
        frecuencias[letra] = frecuencias[letra]/total
    return frecuencias

#Funcion para descrifrar un mensaje cifrado con la clave n
def desencriptar(texto, cantidad_letras):
    texto= texto.upper()
    texto_desencriptado = ""
    for char in texto:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (index - cantidad_letras) % len(alfabeto)
            texto_desencriptado = texto_desencriptado + alfabeto[nuevo_index]
        else:
            texto_desencriptado = texto_desencriptado + char
    return texto_desencriptado

#Funcion para buscar la clave de cifrado que mejor se ajuste a la distribucion de frecuencias
def find_key(text):
    frecuencias = calcular_frecuencias(text)
    min_error = float("inf")
    mejor_key = None
    for key in range(cantidad_letras):
        error = 0
        for letras, frecuencia in frequencias.items():
            index = alfabeto.index(letras)
            new_index = (index + key) % len(alfabeto)
            error += abs(frecuencia - frecuencias[alfabeto[new_index]])
        if error < min_error:
            min_error = error
            mejor_key = key
    return mejor_key


texto = "Hola esto es un texto de prueba para ver si funciona"
print(calcular_frecuencias(texto))
print(desencriptar("vczo sghc sg ibo dfispo", 14))