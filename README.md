# Objetivos del proyecto
1. Análisis de eficiencia: identificar áreas que requieran mayor soporte o capacitación en la mesa de ayuda entre el gran volumen de solicitudes/tickets
2. Segmentación de problemas comunes:  Agrupar problemas similares según el motivo o área afectada, permitiendo soluciones proactivas y la automatización de respuestas
3. Mejora de la experiencia del colaborador: Detectar patrones en los comentarios y el estatus de los colaboradores para mejorar la atención y la satisfacción
4. Predicción de necesidades de soporte: Usar técnicas de minería de datos para anticipar las necesidades de los colaboradores, con el fin de ofrecer soluciones más rápidas y eficientes

## Limpieza, selección y Transformaciones realizadas

#### 1. Renombrar columnas para un tratamiento mas sencillo

#### 2. Eliminación de las siguientes columnas
- Nombre de colaborador
- Motivo uniformes
- Celular
- Regional
- Estatus
- Columna1

#### 3. Detección y Tratamiento de Nulos

a) Eliminar tuplas con valores nulos para las siguientes columnas
- ID
- Sucursal
- fecha
- motivo
- Area buscada

b) Reemplazar valores nulos de ticket por -1

#### 4. Agregar columnas mes y día a partir de la fecha
#### 5. Agregar columna con valor numérico de área buscada


Colab de apoyo: https://colab.research.google.com/drive/16kGQLs3EEDMH4Tt_ja8y-OlhuOpexTwx?usp=sharing#scrollTo=Z0ki4DnK0Q_L

