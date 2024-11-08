import pandas as pd

file_name = 'assets/dataset-mesa-de-ayuda.csv'
data = pd.read_csv(file_name)

print(data.info())

# ETL Methods
## -------------------  -----------------------
def check_null( ds, column: str):
    print("\n\n--- CUENTA DE ATRIBUTOS CON VALORES NULOS")
    print(ds.isnull().sum())

# -------------- Add column month --------------
def add_month_column(data):
    print("\n\n--- AGREGANDO COLUMNA MES")
    split_date = data.ReportDate.str.split(expand=True)
    
    data['ReportDate'] = split_date[0]

    print(data['ReportDate'])

    return data

# -------------- rename columns --------------
def rename_columns(data, column_names: list):
    print('\n\n--- RENOMBAR COLUMNAS')
    for new_column in column_names:
        data = data.rename(columns=new_column)

    #print(data.info())
    return data

# New column names
new_column_names = []
new_column_names.append({'id colaborador':'idColaborador'})
new_column_names.append({'Nombre ':'Nombre'})
new_column_names.append({'Fecha ':'Fecha'})
new_column_names.append({'Regional CH':'RegionalCH'})
new_column_names.append({'Área que busca':'AreaBuscada'})
new_column_names.append({'Celular ':'Celular'})
new_column_names.append({'Motivo de Contacto':'MotivoDeContacto'})
new_column_names.append({'Motivo Uniformes':'MotivoUniformes'})
new_column_names.append({'Estatus ':'Estatus'})


#id colaborador,Nombre ,Fecha ,Sucursal,Puesto,Regional CH,Motivo ,Ticket,Área que busca,Celular ,Motivo de Contacto,Motivo Uniformes,Estatus ,Columna1

check_null(data, "")
data = rename_columns(data, new_column_names)

print(data.info())


