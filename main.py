import pandas as pd

file_name = 'assets/dataset-mesa-de-ayuda.csv'
data = pd.read_csv(file_name)

print(data.info())

# ETL Methods
## -------------------  -----------------------
def check_null( ds):
    print("\n\n--- CUENTA DE ATRIBUTOS CON VALORES NULOS")
    print(ds.isnull().sum())

# -------------- rename columns --------------
def rename_columns(data, column_names: list):
    print('\n\n--- RENOMBAR COLUMNAS')
    print('\n--- Nombres iniciales')
    print(data.info())
    for new_column in column_names:
        data = data.rename(columns=new_column)

    print('\n--- Nombres actuales')
    print(data.info())
    return data

# -------------- Delete columns --------------
def delete_unnecessary_columns(data):
    print('\n\n--- ELIMINANDO COLUMNAS')
    data.drop(columns=['Nombre', 'RegionalCH', 'Celular', 'MotivoDeContacto', 'MotivoUniformes', 'Estatus', 'Columna1'], inplace=True)

    print(data.head())

# -------------- Null treatment --------------
def null_values_treatment(data):
    print('\n\n --- TRATAMIENTO DE VALORES NULOS')
    print('\n --- CUENTA DE ATRIBUTOS CON VALORES NULOS INICIAL\n')
    print(data.isnull().sum())

    data.dropna(subset=['Puesto', 'Sucursal', 'Motivo', 'AreaBuscada'], inplace=True)
    data['Ticket'].fillna(0,inplace=True)

    print('\n --- CUENTA DE ATRIBUTOS CON VALORES NULOS ACTUAL\n')
    print(data.isnull().sum())



def add_searched_area_code_column(data):
    # Crear copia de la columna "Área que busca"
    #data['Copia Área que busca'] = data['Área que busca']
    data['CodigoAreaBuscada'] = data['AreaBuscada']


    # Reemplazar valores por números
    data['CodigoAreaBuscada'].replace({
        'Administración de Personal': 1,
        'Administración de Personal ': 1,
        'Compensaciones y Beneficios': 2,
        'Compensaciones y Beneficios ': 2,
        'Relaciones Laborales': 3,
        'Relaciones Laborales ': 3,
        'Regionales de CH': 4,
        'Regionales de CH ': 4,
        'Uniformes y Epp': 5,
        'Uniformes y Epp ': 5,
        'Universidad Apymsa': 6,
        'Universidad Apymsa ': 6,
        'Otros': 7,
        'Otros ': 7
         
    }, inplace=True)

    #Falta reemplazar los nulos o eliminar
    print("\n\n--- AGREGANDO COLUMNA CODIGO DE AREA BUSCADA")

    print(data.head(20))
    #print(data.info())


# -------------- Add column month and day--------------
def add_month_column(data):
    print("\n\n--- AGREGANDO COLUMNAS MES y DIA")
    split_date = data['Fecha'].str.split('/', expand=True)
    
    #data['ReportDate'] = split_date[0]

    print(split_date[0])

    data['Dia'] = split_date[0]
    data['Mes'] = split_date[0]

    return data

# -------------- Add column month and day (better) --------------
def add_month_column_elegant(data):
    print("\n\n--- AGREGANDO COLUMNAS MES y DIA")
    # Cambiamos a datetime el atributo fecha para hacerlo compatible con operaciones de tiempo
    data['Fecha'] = pd.to_datetime(data['Fecha'], format='%d/%m/%Y')

    # Crear las columnas de Día, Mes y Año
    data['Mes'] = data['Fecha'].dt.month
    data['Dia'] = data['Fecha'].dt.day
    
    #data['Año'] = data['Fecha'].dt.year

    print(data.info())

    return data


# -------------- Generate new CSV --------------
def save_csv(data):
    data.to_csv('assets/dataset-mesa-de-ayuda-cleaned.csv', index=False)

# New column names
new_column_names = []
new_column_names.append({'id colaborador':'idColaborador'})
new_column_names.append({'Nombre ':'Nombre'})
new_column_names.append({'Fecha ':'Fecha'})
new_column_names.append({'Regional CH':'RegionalCH'})
new_column_names.append({'Motivo ':'Motivo'})
new_column_names.append({'Área que busca':'AreaBuscada'})
new_column_names.append({'Celular ':'Celular'})
new_column_names.append({'Motivo de Contacto':'MotivoDeContacto'})
new_column_names.append({'Motivo Uniformes':'MotivoUniformes'})
new_column_names.append({'Estatus ':'Estatus'})


#id colaborador,Nombre ,Fecha ,Sucursal,Puesto,Regional CH,Motivo ,Ticket,Área que busca,Celular ,Motivo de Contacto,Motivo Uniformes,Estatus ,Columna1

check_null(data)

data = rename_columns(data, new_column_names)

delete_unnecessary_columns(data)

null_values_treatment(data)

data = add_month_column_elegant(data)

add_searched_area_code_column(data)

#save_csv(data)