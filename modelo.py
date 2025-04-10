# modelo.py
from dataset import cargar_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Cargar los datos
df = cargar_dataset()

# Variables predictoras y objetivo
X = df[['origen', 'destino', 'hora_salida', 'distancia_km', 'congestion']]
y = df['tiempo_real']

# Preprocesamiento y modelo
preprocesador = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['origen', 'destino', 'congestion'])
    ],
    remainder='passthrough'
)

modelo = Pipeline(steps=[
    ('preprocesador', preprocesador),
    ('regresion', LinearRegression())
])

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento y evaluación
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Error medio absoluto: {mae:.2f} minutos')
