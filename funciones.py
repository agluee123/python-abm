import pandas as pd


def alta_cliente():
    try:
        # Cargamos el archivo csv que ya existe
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)

        # El usuario agrega datos mediante inputs
        dni = int(input("Ingrese el DNI del nuevo cliente: "))
        nombre = str(input("Ingrese el NOMBRE y APELLIDO del nuevo cliente: "))
        edad = int(input("Ingrese la EDAD del nuevo cliente: "))
        direccion = str(input("Ingrese la DIRECCION del nuevo cliente: "))
        telefono = (input("Ingrese su número de TELEFONO: "))
        email = str(input("Ingrese su EMAIL: "))
        preferente = str(
            input("Ingrese si es un cliente preferente, escribir SI O NO: "))

        # Se crea el nuevo registro en forma de diccionario con los nombres de las columnas del dataframe
        nuevo_registro = {'dni': dni, 'nombre': nombre, 'edad': edad, 'direccion': direccion,
                          'telefono': telefono, 'email': email, 'preferente': preferente}

        # El registro lo convertimos en un nuevo dataframe
        nuevo_df = pd.DataFrame([nuevo_registro])

        # Concatenamos el dataframe que ya existe
        df = pd.concat([df, nuevo_df], ignore_index=True)

        # Guardamos el dataframe actualizado en el archivo CSV
        df.to_csv(nombre_archivo, index=False)
    except Exception as e:
        print("Error en dar de alta a un cliente:", e)


def listar_cliente():
    try:
        # Código de la función listar_cliente
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)

        buscar_dato = str(
            input("Ingrese el nombre del cliente que desea buscar: "))

        resultado = df[df['nombre'] == buscar_dato]

        if not resultado.empty:
            print(resultado)
        else:
            print(
                f"No se encontraron registros para el nombre '{buscar_dato}'.")
    except Exception as e:
        print("Error en mostrar el cliente:", e)


def eliminar():
    try:
        # Código de la función eliminar
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)

        # El usuario selecciona el nombre que desea eliminar
        nombre_eliminar = input(
            "Ingrese el NOMBRE del cliente que desea eliminar: ")

        df = df[df['nombre'] != nombre_eliminar]

        df.to_csv(nombre_archivo, index=False)
    except Exception as e:
        print("Error en eliminar al cliente:", e)


def mostrar_nombre_dni():
    try:
        # Código de la función mostrar_nombre_dni
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)
        print(df[['nombre', 'dni']])
    except Exception as e:
        print("Error en mostrar el nombre del cliente:", e)


def mostrar_preferente_nombre_dni():
    try:
        # Código de la función mostrar_preferente_nombre_dni
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)
        clientes_prefentes = df[df['preferente'] == 'si']
        print(clientes_prefentes[['nombre', 'dni']])
    except Exception as e:
        print("Error en mostrar al cliente preferente:", e)


def filtrar_pedros():
    try:
        # Código de la función filtrar_pedros
        nombre_archivo = 'datos_clientes.csv'
        df = pd.read_csv(nombre_archivo)
        personas_pedro = df[df['nombre'].str.lower().str.contains('pedro')]
        print(personas_pedro)
    except Exception as e:
        print("no se pudieron mostrar a los pedros:", e)


def calcular_promedio():
    try:
        # Código de la función calcular_promedio
        datos_clientes = pd.read_csv('datos_clientes.csv')
        promedio_edad = datos_clientes['edad'].mean()
        print("El promedio de edad de los clientes es:", promedio_edad)
    except Exception as e:
        print("no se pudo calcular el pronmedio:", e)


def terminar():
    print("¡Gracias por utilizar el programa de cargar clientes, HASTAA LUEGOOOO!!!!!")
    exit()        
