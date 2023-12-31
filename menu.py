from funciones import alta_cliente
from funciones import eliminar
from funciones import listar_cliente
from funciones import mostrar_nombre_dni
from funciones import mostrar_preferente_nombre_dni
from funciones import filtrar_pedros
from funciones import calcular_promedio
from funciones import terminar

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
    elif opcion == '2':
        eliminar()
    elif opcion == '3':
        listar_cliente()
    elif opcion == '4':
        mostrar_nombre_dni()
    elif opcion == '5':
        mostrar_preferente_nombre_dni()
    elif opcion == '6':
        filtrar_pedros()
    elif opcion == '7':
        calcular_promedio()
    elif opcion == '8':
        terminar()

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
