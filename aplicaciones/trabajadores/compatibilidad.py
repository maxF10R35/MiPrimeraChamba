import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

def evaluar_candidato(d_a_fit, n_s_fit, p_o_fit):
    print('cargando modelo de compatibilidad...')
    try:
        modelo = load_model('.\\aplicaciones\\trabajadores\\static\\MLP\\compatibilidad_candidato.h5')
    except OSError:
        return "Error: No se encuentra el archivo .h5"

    # PASO 2: PREPARAR LOS DATOS (El paso más importante)
    # El modelo espera un TENSOR o ARRAY de forma (N, 3).
    # Aunque sea un solo candidato, debe ir en una lista de listas [[...]]
    datos_entrada = np.array([[d_a_fit, n_s_fit, p_o_fit]])
    
    # PASO 3: PREDECIR
    prediccion = modelo.predict(datos_entrada, verbose=0)
    score = prediccion[0][0] # Extraemos el número del array [[0.85]]
    
    return round(float(score), 4)


'''
# --- EJEMPLO DE USO ---

# Digamos que llegan los datos de un nuevo candidato
resultado = evaluar_candidato(0.85, 0.60, 0.90)

print("-" * 30)
print("REPORTE DE CANDIDATO")
print("-" * 30)
print(f"Score:  {resultado} ")'''