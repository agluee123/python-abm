
import csv

def añadir_cliente(nombre_archivo):
    # se pide al usuario los datos para el ingreso del nuevo cliente
    dni = int(input("Ingrese el DNI del nuevo cliente: "))
    nombre = str(input("Ingrese el NOMBRE del nuevo cliente: "))
    edad = int(input("Ingrese la EDAD del nuevo cliente: "))
    direccion = str(input("Ingrese la DIRECCION del nuevo cliente: "))
    telefono = input("Ingrese su número de TELEFONO: ")
    email = input("Ingrese su EMAIL: ")
    preferente = str(input("Ingrese si es un cliente preferente, escribir SI O NO: "))

    
    with open(nombre_archivo, "a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([dni, nombre, edad, direccion, telefono, email, preferente])

nombre_archivo_csv = "datos_clientes.csv"



def eliminar_cliente(nombre_archivo, campo, valor):
    campo = campo.lower()
    campos_validos = ['dni', 'nombre', 'edad', 'direccion', 'telefono', 'email', 'preferente']

    if campo not in campos_validos:
        print(f"Campo '{campo}' no válido. Los campos válidos son: {', '.join(campos_validos)}")
        return

    registros_actualizados = []
    cliente_encontrado = False

    with open(nombre_archivo, 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for registro in reader:
            if registro[campos_validos.index(campo)] == str(valor):
                cliente_encontrado = True
            else:
                registros_actualizados.append(registro)

    if cliente_encontrado:
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerows(registros_actualizados)
        print(f"Cliente con {campo.upper()} '{valor}' ha sido dado de baja.")
    else:
        print(f"Cliente con {campo.upper()} '{valor}' no encontrado. No se realizó ninguna acción.")

# Ejemplo de uso
nombre_archivo_csv = 'datos_clientes.csv'
#campo_a_buscar = input("Ingrese el campo por el cual desea dar de baja al cliente (dni, nombre, edad, direccion, telefono, email, preferente): ")
#valor_a_buscar = input(f"Ingrese el valor del {campo_a_buscar.upper()} del cliente que desea dar de baja: ")

#eliminar_cliente(nombre_archivo_csv, campo_a_buscar, valor_a_buscar)






