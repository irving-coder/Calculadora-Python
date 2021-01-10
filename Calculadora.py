entrada1 = 8
entrada2 = 5

def suma(ent1, ent2):
    return ent1 + ent2

def resta(ent1, ent2):
    return ent1 - ent2

def producto(ent1, ent2):
    return ent1 * ent2

def division(ent1, ent2):
    return ent1 / ent2

print('La suma de '+ str(entrada1) +' + '+ str(entrada2) +' es: '+ str(suma(entrada1, entrada2)))
print('La resta de '+ str(entrada1) +' - '+ str(entrada2) +' es: '+ str(resta(entrada1, entrada2)))
print('El producto de '+ str(entrada1) +' x '+ str(entrada2) +' es: '+ str(producto(entrada1, entrada2)))
print('La división de '+ str(entrada1) +' - '+ str(entrada2) +' es: '+ str(division(entrada1, entrada2)))