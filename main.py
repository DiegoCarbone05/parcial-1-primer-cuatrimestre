import funciones as f

existencias = [
    ["PBA", 'autos', 39854],
    ["PBA", 'muñecas', 44857],
    ["PBA", 'trenes', 22412],
    ["PBA", 'peluches', 512],
    ['CABA', 'autos', 312],
    ['CABA', 'spinners', 50455],
    ['CABA', 'cartas', 784],
    ['CABA', 'peluches', 47784],
    ['Chubut', 'trenes', 4113],
    ['Chubut', 'autos', 9684],
    ['Chubut', 'spinners', 2110],
    ['Chubut', 'peluches', 4141],
    ['Tucumán', 'trenes', 41],
    ['Tucumán', 'cartas', 677],
    ['Tucumán', 'autos', 11],
    ['Tucumán', 'peluches', 45874],
    ['Mendoza', 'muñecas', 141],
    ['Mendoza', 'cartas', 252],
    ['Mendoza', 'autos', 454],
    ['Mendoza', 'peluches', 54423],
]
continuar = 's'

while continuar == 's':
    f.menu(existencias)
    print('')
    continuar = input('Continuar? (s/n): ')
