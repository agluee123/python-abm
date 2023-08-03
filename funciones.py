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
    telefono = int(input("Ingrese su número de TELEFONO: "))
    email = str(input("Ingrese su EMAIL: "))
    preferente = str(input("Ingrese si es un cliente preferente, escribir SI O NO: "))

    #se crea el nuevo registro en forma de diccionario con los nombres de las columnas del dataframe
    nuevo_registro={'dni':dni, 'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono, 'email':email, 'preferente':preferente}

    #el registro lo convertimos en un nuevo dataframe
    nuevo_df=pd.DataFrame([nuevo_registro])

    #concatenamos el dataframe que ya existe
    df=pd.concat([df,nuevo_df],ignore_index=True)

    #guardamos el dataframe actualizado en el archivo CSV
    df.to_csv(nombre_archivo, index=False)


def listar_cliente():
        
        nombre_archivo='datos_clientes.csv'
        df=pd.read_csv(nombre_archivo)


        buscar_dato=str(input("ingrese el nombre del cliente que desea buscar: "))

        resultado=df[df['nombre']==buscar_dato]

        if not resultado.empty:
                print(resultado)
        else:
                print(f"No se encontraron registros para el nombre '{buscar_dato}'.") 


def eliminar():
    #cargamos el archivo csv existente
    nombre_archivo='datos_clientes.csv'
    df=pd.read_csv(nombre_archivo)


    #el usuario seleciione el nombre que desea eliminar
    nombre_eliminar=input("ingrese el NOMBRE del cliente que desea eliminar: ")

    df = df[df['nombre'] != nombre_eliminar]

    df.to_csv(nombre_archivo, index=False)


def mostrar_nombre_dni():
        nombre_archivo='datos_clientes.csv'
        df= pd.read_csv(nombre_archivo)
        print(df[['nombre','dni']])
        
        
def mostrar_preferente_nombre_dni():
        nombre_archivo='datos_clientes.csv'
        df=pd.read_csv(nombre_archivo)
        clientes_prefentes=df[df['preferente']=='si']
        print(clientes_prefentes[['nombre','dni']])        
        

def filtrar_pedros():
        nombre_archivo='datos_clientes.csv'
        df=pd.read_csv(nombre_archivo)
        personas_pedro = df[df['nombre'].str.lower().str.contains('pedro')]
        print(personas_pedro)





