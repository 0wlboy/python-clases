import os 
import time

def agregar(lista):
  nombre = input('Nombre del producto: ')
  while nombre == '' :
    print('El nombre no deberia de quedar vacio.')
    nombre = input('Nombre de Producto: ')
  
  precio = 0
  while precio <= 0: 
    try: 
      precio = float(input('Precio de producto en decimales '))
      if precio <= 0:
        print('Ingrese un numero mayor a 0')
    except ValueError:
      print('Ingrese un numero decimal valido valido')

  cantidad = 0
  while cantidad <= 0: 
    try:
      cantidad = int(input('Cantidad de producto: '))
      if cantidad <= 0: 
        print('Porfavor ingrese una cantidad mayor a 0')
    except ValueError:
      print('Ingrese un numero entero valido')
  
  item = {
    'nombre': nombre, 
    'precio': precio, 
    'cantidad': cantidad
  }
  lista.append(item)
  print('Producto añadido correctamente.')
  time.sleep(1)


def eliminar(lista):
  if len(lista) == 0:
    print('No hay productos en la lista.')
    return
  while True: 
    try: 
      indice = int(input('Ingrese el indice del producto a eleminar: '))
      if (0 <=indice < len(lista)): 
        del lista[indice]
        print('Producto eleminado correctamente')
        break
      print('Fuera de rango')
    except ValueError:
      print('Ingrese un numero entero valido') 
  time.sleep(1)

def verLista(lista):
  if len(lista) == 0:
    print('No hay elementos en la lista')
    return
  print('Inventario: ')
  print("--------------------------------------------------")
  print("{:<5} {:<20} {:<10} {:<10}".format("Índice", "Nombre", "Precio $", "Cantidad"))
  print("--------------------------------------------------")
  for i, producto in enumerate(lista):
    print("{:<5} {:<20} {:<10.2f} {:<10}".format(i, producto["nombre"], producto["precio"], producto["cantidad"]))
  print("--------------------------------------------------")
  time.sleep(1)

lista = []

print('Bienvienido a Inventarie OS.')
while (True):
  print('1)Ingresar nuevo producto\n2)Eliminar producto\n3)Ver lista de producto\n4)Salir')
  while True: 
    opcion = input('Ingrese un numero correspondiente a las opciones ya dadas: ')
    if opcion in ('1','2','3','4'):
      break
    print('Porfavor ingrese un numero valido')
  time.sleep(1)
  os.system('cls')
  if(opcion == '1'):
    agregar(lista)
  elif(opcion == '2'):
    eliminar(lista)
  elif (opcion == '3'):
    verLista(lista)
  elif (opcion == '4'):
    print('Adios. ')
    time.sleep(3)
    os.system('cls')
    break
  input('Precione enter para continuar...')
  print('Limpiando pantalla')
  time.sleep(3)
  os.system('cls')
