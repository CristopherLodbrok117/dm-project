# Importar las librerías necesarias
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
file_path = "C:/Users/andri/Downloads/dataset-mesa-de-ayuda-cleaned.csv"
dataset = pd.read_csv(file_path)

# Paso 1: Codificar la columna 'Motivo' en valores numéricos
label_encoder = LabelEncoder()
dataset['Motivo_encoded'] = label_encoder.fit_transform(dataset['Motivo'])

# Paso 2: Seleccionar características y variable objetivo para KNN
X = dataset[['Motivo_encoded', 'CodigoAreaBuscada']]
y = dataset['CodigoAreaBuscada']

# Paso 3: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Paso 4: Inicializar el modelo KNN y entrenarlo
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Paso 5: Realizar predicciones y evaluar el modelo
y_pred = knn.predict(X_test)
print("Reporte de Clasificación:\n", classification_report(y_test, y_pred))

# Obtener los valores únicos de 'Motivo' con su correspondiente valor codificado
motivo_encoded_mapping = dict(zip(dataset['Motivo'], dataset['Motivo_encoded']))
unique_motivo_encoded = pd.DataFrame(motivo_encoded_mapping.items(), columns=['Motivo', 'Motivo_encoded'])

# Mostrar el mapeo de motivos originales a valores codificados
print(unique_motivo_encoded.sort_values(by='Motivo_encoded').reset_index(drop=True))

# Paso 6: Visualización de los clusters
# Mapear los valores codificados de 'Motivo_encoded' a sus etiquetas originales
motivo_labels = label_encoder.inverse_transform(X_test['Motivo_encoded'].unique())
motivo_mapping = dict(zip(X_test['Motivo_encoded'].unique(), motivo_labels))

# Ajustar el gráfico para mejor visualización
plt.figure(figsize=(15, 8))
sns.scatterplot(
    x=X_test['Motivo_encoded'].map(motivo_mapping),  # Mapear los valores codificados a etiquetas originales
    y=y_test,
    hue=y_pred,
    palette="viridis",
    s=100,
    alpha=0.7
)

plt.title('Segmentación de Problemas Comunes: Motivo vs Código de Área')
plt.xlabel('Motivo')
plt.ylabel('Código de Área Buscada')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mayor claridad
plt.legend(title='Área Predicha por KNN', loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()  # Ajustar el diseño para evitar cortes en etiquetas
plt.show()
