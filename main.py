import pandas as pd

file_name = 'dataset-mesa-de-ayuda.csv'
data = pd.read_csv(file_name)

print(data.info())