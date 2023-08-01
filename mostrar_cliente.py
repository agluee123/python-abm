import pandas as pd


def listar_cliente():
        
        nombre_archivo='datos_clientes.csv'
        df=pd.read_csv(nombre_archivo)


        buscar_dato=str(input("ingrese el nombre del cliente que desea buscar: "))

        resultado=df[df['nombre']==buscar_dato]

        if not resultado.empty:
                print(resultado)
        else:
                print(f"No se encontraron registros para el nombre '{buscar_dato}'.")     