def menu(existencias):
    print('')
    print('***************************')
    print('MENU PRNCIPAL')
    print('')
    print('Seleccione la operacion que desea usar:')
    print('(1) Calcular Inventario')
    print('(2) Calcular ubicacion con bajo stock')
    print('(3) Obtener ubicacion con mayor cantidad de stock')
    print('(4) Cantidad de depósitos que hayan almacenado más de 50.000 unidades')
    print('(5) Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados')
    
    print('')
    numero_operacion = int(input('Seleccione su operación: '))
    
    match numero_operacion:
        case 1:
            calcular_inventario(existencias)
        case 2:
            calcular_bajo_stock(existencias)
        case 3:
            obtener_mayor_cant_juguetes(existencias)
        case 4:
            punto_6(existencias)
        case 5:
            punto_7(existencias)

def calcular_inventario(existencias:list, disableUI:bool = False)-> list:
    
    total_inventario = [
        ["PBA", 0],
        ["CABA", 0],
        ["Chubut", 0],
        ["Tucumán", 0],
        ["Mendoza", 0],
    ]
    
    for item in existencias:
        match item[0]:
            case 'PBA':
                total_inventario[0][1] += item[2]
            case 'CABA':
                total_inventario[1][1] += item[2]
            case 'Chubut':
                total_inventario[2][1] += item[2]
            case 'Tucumán':
                total_inventario[3][1] += item[2]
            case 'Mendoza':
                total_inventario[4][1] += item[2]
                
    if not(disableUI):
        print('')
        print('****************')
        print('Cantidad total de juguetes almacenados entre todos los tipos: ')
        for item in total_inventario:
            print(f'{item[0]}: {item[1]}')
        
    return total_inventario

def calcular_bajo_stock(existencias:list)-> list:
    
    productos_bajo_stock = []
    
    for item in existencias:
        if item[2] < 500:
            productos_bajo_stock += [[item[0], item[1]]]
    
    print('')
    print('****************')
    print('Nombres de los juguetes que es necesario reponer en cada depósito: ')
    for item in productos_bajo_stock:
        print(f'{item[0]}: {item[1]}')
    
def obtener_mayor_cant_juguetes(existencias:list)-> list:
    
    mayor_cant_existencias = [
        ['autos'],
        ['muñecas'],
        ['trenes'],
        ['spinners'],
        ['cartas'],
        ['peluches'],
    ]
    
    for item in existencias:
        match item[1]:
            case 'autos':
                if len(mayor_cant_existencias[0]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[0][1][2]:
                        mayor_cant_existencias[0][1] = item
                else:
                    mayor_cant_existencias[0] += [item]
            case 'muñecas':
                if len(mayor_cant_existencias[1]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[1][1][2]:
                        mayor_cant_existencias[1][1] = item
                else:
                    mayor_cant_existencias[1] += [item]
            case 'trenes':
                if len(mayor_cant_existencias[2]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[2][1][2]:
                        mayor_cant_existencias[2][1] = item
                else:
                    mayor_cant_existencias[2] += [item]
            case 'spinners':
                if len(mayor_cant_existencias[3]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[3][1][2]:
                        mayor_cant_existencias[3][1] = item
                else:
                    mayor_cant_existencias[3] += [item]
            case 'cartas':
                if len(mayor_cant_existencias[4]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[4][1][2]:
                        mayor_cant_existencias[4][1] = item
                else:
                    mayor_cant_existencias[4] += [item]
            case 'peluches':
                if len(mayor_cant_existencias[5]) > 1: # Si es la primera vez
                    if item[2] > mayor_cant_existencias[5][1][2]:
                        mayor_cant_existencias[5][1] = item
                else:
                    mayor_cant_existencias[5] += [item]
                    
    print('')
    print('****************')
    print('Máxima cantidad de juguetes almacenados de cada tipo:')
    for item in mayor_cant_existencias:
        print(f'{item[0]}: {item[1][0]}, {item[1][2]}') 

def punto_6(existencias:list)-> list:
    
    depositos_stock_mayor = []
        
    for item in calcular_inventario(existencias, True):
        if item[1] > 50000:
            depositos_stock_mayor += [item]
            
    print('')
    print('****************')
    print(f'Depósitos que hayan almacenado más de 50.000 unidades ({len(depositos_stock_mayor)}):')
    for item in depositos_stock_mayor:
        print(f'Deposito: {item[0]}, Unidades: {item[1]}')

def punto_7(existencias:list):
    total_juguetes = calcular_inventario(existencias, True)
    inventario_global = cantidad_global_x_juguete(existencias)
    total_inventario = 0
    
    for item in total_juguetes:
        total_inventario += item[1]


    print((inventario_global[1][1] *100) / total_inventario)
    
    
    print('')
    print('****************')
    print('Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados:')
    
    for item in inventario_global:
        print(f'{item[0]}: {(item[1] *100) / total_inventario}%')

def cantidad_global_x_juguete(existencias:list):
    juguetes = [
        ['autos', 0],
        ['muñecas', 0],
        ['trenes', 0],
        ['spinners', 0],
        ['cartas', 0],
        ['peluches', 0],
    ]
    
    for item in existencias:
        match item[1]:
            case 'autos':
                juguetes[0][1] += item[2]
            case 'muñecas':
                juguetes[1][1] += item[2] 
            case 'trenes':
                juguetes[2][1] += item[2] 
            case 'spinners':
                juguetes[3][1] += item[2] 
            case 'cartas':
                juguetes[4][1] += item[2] 
            case 'peluches':
                juguetes[5][1] += item[2]     
    return (juguetes)
