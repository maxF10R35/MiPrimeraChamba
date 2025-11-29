import numpy as np
import os
from django.conf import settings
import tensorflow as tf

# 1. Definir la ruta absoluta al modelo
# Asumiendo que el archivo 'modelo_mlp.h5' está en la misma carpeta que este script (compatibilidad.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'compatibilidad_candidato.h5')

# Variable global para cargar el modelo una sola vez (eficiencia)
_modelo_cargado = None

def cargar_modelo():
    global _modelo_cargado
    if _modelo_cargado is not None:
        return _modelo_cargado

    if os.path.exists(MODEL_PATH):
        try:
            print(f"Cargando modelo desde: {MODEL_PATH}")
            _modelo_cargado = tf.keras.models.load_model(MODEL_PATH)
            return _modelo_cargado
        except Exception as e:
            print(f"Error al cargar el modelo .h5: {e}")
            return None
    else:
        print(f"ADVERTENCIA: No se encontró el archivo del modelo en {MODEL_PATH}")
        return None



def evaluar_candidato(d_a_fit, n_s_fit, p_o_fit):
    """
    Función principal que usa el modelo.
    Si el modelo falla, devuelve un promedio simple como fallback.
    """
    modelo = cargar_modelo()
    
    if modelo is None:
        # LÓGICA DE RESPALDO (Fallback)
        # Si no hay IA, usamos el promedio matemático simple
        print("Usando cálculo manual por falta de modelo.")
        promedio = (d_a_fit + n_s_fit + p_o_fit) / 3
        return round(float(promedio), 4)
    
    # ... Aquí iría tu lógica de predicción con el modelo real ...
    datos_entrada = np.array([[d_a_fit, n_s_fit, p_o_fit]])
    prediccion = modelo.predict(datos_entrada, verbose=0)
    score = prediccion[0][0] # Extraemos el número del array [[0.85]]
    
    return round(float(score), 4)
    # prediccion = modelo.predict([datos])
    # return prediccion



'''
def evaluar_candidato(d_a_fit, n_s_fit, p_o_fit):
    print('cargando modelo de compatibilidad...')
    try:
        modelo = load_model('.\\aplicaciones\\trabajadores\\compatibilidad_candidato.h5')
    except OSError:
        return "Error: No se encuentra el archivo .h5"

    # PASO 2: PREPARAR LOS DATOS (El paso más importante)
    # El modelo espera un TENSOR o ARRAY de forma (N, 3).
    # Aunque sea un solo candidato, debe ir en una lista de listas [[...]]
    datos_entrada = np.array([[d_a_fit, n_s_fit, p_o_fit]])
    
    # PASO 3: PREDECIR
    prediccion = modelo.predict(datos_entrada, verbose=0)
    score = prediccion[0][0] # Extraemos el número del array [[0.85]]
    
    return round(float(score), 4)'''


'''
# --- EJEMPLO DE USO ---

# Digamos que llegan los datos de un nuevo candidato
resultado = evaluar_candidato(0.85, 0.60, 0.90)

print("-" * 30)
print("REPORTE DE CANDIDATO")
print("-" * 30)
print(f"Score:  {resultado} ")'''