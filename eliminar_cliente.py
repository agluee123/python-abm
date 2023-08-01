import pandas as pd


def eliminar():
    #cargamos el archivo csv existente
    nombre_archivo='datos_clientes.csv'
    df=pd.read_csv(nombre_archivo)


    #el usuario seleciione el nombre que desea eliminar
    nombre_eliminar=input("ingrese el NOMBRE del cliente que desea eliminar: ")

    df = df[df['nombre'] != nombre_eliminar]

    df.to_csv(nombre_archivo, index=False)
