# dataset.py
import pandas as pd

def cargar_dataset():
    data = {
        'origen': ['A', 'A', 'B', 'B', 'C', 'D', 'E'],
        'destino': ['B', 'C', 'D', 'E', 'D', 'E', 'F'],
        'hora_salida': [7, 8, 7, 9, 8, 9, 10],
        'hora_llegada': [7.5, 8.7, 7.6, 9.5, 8.5, 9.4, 10.8],
        'distancia_km': [5, 7, 6, 8, 4, 3, 6],
        'medio_transporte': ['bus', 'bus', 'bus', 'bus', 'bus', 'bus', 'bus'],
        'congestion': ['media', 'alta', 'baja', 'media', 'alta', 'baja', 'media'],
        'tiempo_real': [35, 45, 25, 40, 50, 20, 40]
    }

    df = pd.DataFrame(data)
    return df
