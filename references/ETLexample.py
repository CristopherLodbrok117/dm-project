## Chavez Lazaro Jorge Cristopher Alexis

import pandas as pd

# 1) -------------- rename columns --------------
def rename_columns(data, column_names: list):
    print('\n\n--- RENAMING COLUMNS')
    for new_column in column_names:
        data = data.rename(columns=new_column)

    #print(data.info())
    return data

# 2) -------------- Fill null crime codes with -1 --------------
def fill_null_crimes(data):
    print('\n\n--- FILLING EMPTY CRIMES')
    data['AdditionalCrime1'].fillna(0, inplace=True)
    data['AdditionalCrime2'].fillna(0, inplace=True)
    data['AdditionalCrime3'].fillna(0, inplace=True)

    return data


# 3) -------------- Concatenate additional crimes --------------
def join_additional_crimes(data):
    print("\n\n--- CONCATENATING ADDITIONAL CRIMES")
    data['AdditionalCrimes'] = '' + data['AdditionalCrime1'].astype(str) + ' | ' + data['AdditionalCrime2'].astype(str)  + ' | ' + data['AdditionalCrime3'].astype(str) 

    return data


# 4) -------------- Add age range ---------------
def add_age_range(data):
    print("\n\n--- ADDING AGE RANGE")
    bins = [0, 18, 50, 90]
    labels = ['Young', 'Adult', 'old']
    data['AgeRange'] = pd.cut(data['VictimAge'], bins=bins, labels=labels)


# 5) -------------- Replace datetime with date only --------------
def remove_time_from_date(data):
    print("\n\n--- REPLACING DATETIME WITH DATE")
    split_date = data.ReportDate.str.split(expand=True)
    
    data['ReportDate'] = split_date[0]

    print(data['ReportDate'])

    return data

# 6) -------------- Drop records with no crime defined (11 records) --------------
def remove_records_without_crimes(data):
    print("\n\n--- DELETING RECORDS WITH NO CRIME")

    print(f'Initial count: {data.shape[0]}')
    data.dropna(subset=['CrimeCommited'], inplace=True)
    print(f'Filtered count: {data.shape[0]}')

# 7) -------------- Add delimiters to Modus operandi codes --------------
def add_separators(data):
    print("\n\n--- ADDING DELIMETERS TO MODUS OPERANDI CODES")
    data['ModusOperandi'] = data['ModusOperandi'].str.replace(' ',' - ', regex=False)

    return data

# 8) -------------- Filter records by range --------------
def filter_records_by_age_range(data, minAge: int=1, maxAge=100):
    print("\n\n--- FILTER BY AGE RANGE")

    print(f'Initial count: {data.shape[0]}')
    data = data[(data['VictimAge'] >= minAge) & (data['VictimAge'] <= maxAge)]
    print(f'Filtered count: {data.shape[0]}')

    return data

    

# 9) -------------- Filter records by date --------------
def filter_records_reported_after_date(data, myDate: str):
    print("\n\n--- FILTER RECORDS BY DATE")

    print(f'Initial count: {data.shape[0]}')
    data = data[data['ReportDate'] >= myDate]
    print(f'Filtered count: {data.shape[0]}')

    return data


# 10) -------------- Delete unnecessary COLUMNS -------------- 
def delete_unnecessary_columns(data, columns: list):
    print("\n\n--- DELETING UNNECESSARY COLUMNS")
    
    data = data.drop(columns, axis=1)
    print(data.info())

    return data

def save_csv(data):
    data.to_csv('Cleaned - Crime_Data.csv', index=False)



def save_json(data):
    data.to_json('Cleaned - Crime_Data.json', orient='records', lines=False)


def check_null( ds, column: str):
    print(ds.isnull().sum())


file_name = 'Crime_Data_from_2020_to_Present.csv'
data = pd.read_csv(file_name)

# New column names
new_column_names = []
new_column_names.append({'Date Rptd':'ReportDate'})
new_column_names.append({'DATE OCC':'DateOccured'})
new_column_names.append({'TIME OCC':'TimeOccured'})
new_column_names.append({'Crm Cd':'CrimeCode'})
new_column_names.append({'Crm Cd Desc':'CrimeType'})
new_column_names.append({'Mocodes':'ModusOperandi'})
new_column_names.append({'Vict Age':'VictimAge'})
new_column_names.append({'Vict Sex':'VictimSex'})
new_column_names.append({'Premis Cd':'PlaceType'})
new_column_names.append({'Premis Desc':'PlaceDecription'})
new_column_names.append({'Crm Cd 1':'CrimeCommited'})
new_column_names.append({'Crm Cd 2':'AdditionalCrime1'})
new_column_names.append({'Crm Cd 3':'AdditionalCrime2'})
new_column_names.append({'Crm Cd 4':'AdditionalCrime3'})
new_column_names.append({'LAT':'Latitude'})
new_column_names.append({'LON':'Longtitute'})



# ----------------- Execute ETL methods --------------------
data = rename_columns(data, new_column_names)

data = fill_null_crimes(data)

data = join_additional_crimes(data)

add_age_range(data)

print(data.isnull().sum())
remove_records_without_crimes(data)
print(data.isnull().sum())

remove_time_from_date(data)

data = add_separators(data)

data = filter_records_by_age_range(data)

data = filter_records_reported_after_date(data, '01/01/2023')

data = delete_unnecessary_columns(data, ['AdditionalCrime1', 'AdditionalCrime2', 'AdditionalCrime3'])

# Save files
save_csv(data)
save_json(data)