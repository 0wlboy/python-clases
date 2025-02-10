import os 
import time 

class Tarea:
  def __init__(self, titulo, descripcion):
    self.titulo = titulo
    self.descripcion = descripcion
    self.completado = False
  
  def modificar(self):
    print(f"Modificando tarea: {self.titulo}")

    nuevo_titulo = input('Nuevo título (dejar en blanco para no cambiar): ')
    if nuevo_titulo:  
      self.titulo = nuevo_titulo

    nueva_descripcion = input('Nueva descripción (dejar en blanco para no cambiar): ')
    if nueva_descripcion:  
      self.descripcion = nueva_descripcion

    print('Tarea modificada correctamente.')

  def completar(self): 
    if self.completado: 
        print('Esta tarea ya esta completada')
    else: 
       self.completado = True
       print('La tarea a sido completada!')
  


def agregar(lista):
  titulo = input('Titulo de tarea: ')
  while titulo == '' :
    print('El titulo no deberia de quedar vacio.')
    titulo = input('titulo de tarea: ')
  
  descripcion = input('Descripcion de tarea: ')
  while descripcion == '' :
    print('La descripcion no deberia de quedar vacia.')
    descripcion = input('Descripcion de tarea: ')

  item = Tarea(titulo, descripcion)
  lista.append(item)
  print('Tarea añadida correctamente.')
  time.sleep(1)

def eliminar(lista):
  verLista(lista)
  while True: 
    try: 
      indice = int(input('Ingrese el indice de la tarea a eleminar: '))
      if (0 <=indice < len(lista)): 
        del lista[indice]
        print('Tarea eleminado correctamente')
        break
      print('Fuera de rango')
    except ValueError:
      print('Ingrese un numero entero valido') 
  time.sleep(1)

def verLista(lista):
    if len(lista) == 0:
        print('No hay tareas en la lista')
        return
    print('Tareas: ')
    print("--------------------------------------------------")
    print("{:<5} {:<20} {:<30} {:<20}".format("Índice", "Titulo", "Descripcion", "Estado"))  # Encabezados con más espacio
    print("--------------------------------------------------")
    for i, tarea in enumerate(lista):  # Itera directamente sobre los objetos Tarea
        estado = 'Completado' if tarea.completado else 'No completado'
        print("{:<5} {:<20} {:<30} {:<10}".format(i, tarea.titulo, tarea.descripcion, estado))  # Accede a los atributos del objeto
    print("--------------------------------------------------")
    time.sleep(1)

def verListaCompletados(lista):
    if len(lista) == 0:
        print('No hay tareas en la lista')
        return
    print('Tareas: ')
    print("--------------------------------------------------")
    print("{:<5} {:<20} {:<30} {:<20}".format("Índice", "Titulo", "Descripcion", "Estado"))  # Encabezados con más espacio
    print("--------------------------------------------------")
    for i, tarea in enumerate(lista):  # Itera directamente sobre los objetos Tarea
        if tarea.completado:  
          print("{:<5} {:<20} {:<30} {:<10}".format(i, tarea.titulo, tarea.descripcion, 'Completado'))  # Accede a los atributos del objeto
    print("--------------------------------------------------")
    time.sleep(1)

def verListaNoCompletados(lista):
    if len(lista) == 0:
        print('No hay tareas en la lista')
        return
    print('Tareas: ')
    print("--------------------------------------------------")
    print("{:<5} {:<20} {:<30} {:<20}".format("Índice", "Titulo", "Descripcion", "Estado"))  # Encabezados con más espacio
    print("--------------------------------------------------")
    for i, tarea in enumerate(lista):  # Itera directamente sobre los objetos Tarea
        if not tarea.completado:  
          print("{:<5} {:<20} {:<30} {:<10}".format(i, tarea.titulo, tarea.descripcion, 'No completado'))  # Accede a los atributos del objeto
    print("--------------------------------------------------")
    time.sleep(1)


def seleccion(lista,num):
  verLista(lista)
  print('')
  print('')
  if num == 4: 
     accion = 'completar'
  else:
     accion = 'modificar'
  while True: 
    try: 
      indice = int(input(f'Ingrese el indice de la tarea a {accion}: '))
      if 0 <= indice < len(lista):
        tarea = lista[indice]
        if num == 4:
          tarea.completar()
        else:
           tarea.modificar()
        break 
      print('Fuera de rango');
    except ValueError:
      print('Ingresa un numero entero valido')
  time.sleep(1)


lista = []

print('Bienvienido a Tareas OS.')
while (True):
  print('1)Ingresar Nueva Tarea\n2)Eliminar Tarea\n3)Ver Todas las Tareas \n4)Marcar una Tarea como Completada \n5)Ver Tareas Completadas \n6)Ver Tareas Pendientes \n7)Modificar una Tarea \n8)Salir')
  while True: 
    opcion = input('Ingrese un numero correspondiente a las opciones ya dadas: ')
    if opcion in ('1','2','3','4','5','6','7','8'):
      break
    print('Porfavor ingrese un numero valido')
  time.sleep(1)
  os.system('cls')
  match opcion: 
    case '1':
      agregar(lista)
    case '2':
      eliminar(lista)
    case '3':
      verLista(lista)
    case '4':
        seleccion(lista,opcion)
    case '5':
        verListaCompletados(lista)
    case '6':
        verListaNoCompletados(lista)
    case '7':
        seleccion(lista,opcion)
    case '_':
      print('Adios. ')
      time.sleep(3)
      os.system('cls')
      break
  input('Precione enter para continuar...')
  print('Limpiando pantalla')
  time.sleep(3)
  os.system('cls')