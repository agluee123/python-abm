from agregar_cliente import alta_cliente
from eliminar_cliente import eliminar
from mostrar_cliente import listar_cliente


while True:
    print("\nMENU:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar datos de un cliente")
    print("4. Listar todos los clientes con nombre y DNI")
    print("5. Listar clientes preferentes con nombre y DNI")
    print("6. Listar todas las personas que se llaman Pedro")
    print("7. Calcular el promedio de Edad de los clientes")
    print("8. Terminar")

    opcion = input("Seleccione una opción (1-8): ")

    if opcion == '1':
        alta_cliente()
    elif opcion=='2':
        eliminar()
    elif opcion=='3':
        listar_cliente()    
            
        
        