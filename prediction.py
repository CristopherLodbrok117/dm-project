import pandas as pd



clean_file_name = 'assets/dataset-mesa-de-ayuda-cleaned.csv'
data = pd.read_csv(clean_file_name)

def check_if_column_is_numeric(data, name):
    if data[name].str.isnumeric().all():
    # Convertir la columna a tipo int32
        #data[name] = data[name].astype('int64')
        print(f"TODOS NUMERICOS: {name}")
    else:
        print(f"Existen valores no numéricos en la columna {name}")

def print_unique_values(data, name):
    unique_names = data[name].unique()

    print(f"\n\n{name} values:", unique_names)

print(data.info())

#check_if_column_is_numeric(data, 'CodigoAreaBuscada')
#print_unique_values(data, 'CodigoAreaBuscada')

