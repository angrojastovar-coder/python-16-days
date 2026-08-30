my_list = [555, 99, 800]

def revisar_3_cifras(list):
    list_3_digitos = []
    for l in list:
        if l in range(100,1000):
            list_3_digitos.append(l)
    return list_3_digitos
    
resultado = revisar_3_cifras(my_list)
print(resultado)