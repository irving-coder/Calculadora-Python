entrada1 = 34
entrada2 = 13

# Función suma
def suma(ent1, ent2):
    return ent1 + ent2

# Función resta
def resta(ent1, ent2):
    return ent1 - ent2

# Función producto
def producto(ent1, ent2):
    return ent1 * ent2

# Función división
def division(ent1, ent2):
    return ent1 / ent2

print('La suma de '+ str(entrada1) +' + '+ str(entrada2) +' es: '+ str(suma(entrada1, entrada2)))
print('La resta de '+ str(entrada1) +' - '+ str(entrada2) +' es: '+ str(resta(entrada1, entrada2)))
print('El producto de '+ str(entrada1) +' x '+ str(entrada2) +' es: '+ str(producto(entrada1, entrada2)))
print('La división de '+ str(entrada1) +' - '+ str(entrada2) +' es: '+ str(division(entrada1, entrada2)))
print('Adios')