#importamos la biblioteca pandas
import pandas as pd


def alta_cliente():
    #cargamos el archivo csv que ya existe
    nombre_archivo='datos_clientes.csv'
    df=pd.read_csv(nombre_archivo)


    #el usuario agrega datos mediante inputs
    dni = int(input("Ingrese el DNI del nuevo cliente: "))
    nombre = str(input("Ingrese el NOMBRE del nuevo cliente: "))
    edad = int(input("Ingrese la EDAD del nuevo cliente: "))
    direccion = str(input("Ingrese la DIRECCION del nuevo cliente: "))
    telefono = input("Ingrese su número de TELEFONO: ")
    email = input("Ingrese su EMAIL: ")
    preferente = str(input("Ingrese si es un cliente preferente, escribir SI O NO: "))

    #se crea el nuevo registro en forma de diccionario con los nombres de las columnas del dataframe
    nuevo_registro={'dni':dni, 'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono, 'email':email, 'preferente':preferente}

    #el registro lo convertimos en un nuevo dataframe
    nuevo_df=pd.DataFrame([nuevo_registro])

    #concatenamos el dataframe que ya existe
    df=pd.concat([df,nuevo_df],ignore_index=True)

    #guardamos el dataframe actualizado en el archivo CSV
    df.to_csv(nombre_archivo, index=False)

