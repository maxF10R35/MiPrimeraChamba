# aplicaciones/utils.py
from django.conf import settings
from cryptography.fernet import Fernet

# Cargamos la clave desde settings (que a su vez la lee del .env)
# Si da error, asegúrate de haber seguido el paso de settings.py anterior
cipher = Fernet(settings.CLAVE_ENCRIPTACION)

def encriptar(texto_plano):
    if not texto_plano: return None
    # Convertimos a bytes, encriptamos y devolvemos como string para la BD
    return cipher.encrypt(str(texto_plano).encode('utf-8')).decode('utf-8')

def desencriptar(texto_encriptado):
    if not texto_encriptado: return None
    try:
        # Convertimos a bytes, desencriptamos y devolvemos string limpio
        return cipher.decrypt(str(texto_encriptado).encode('utf-8')).decode('utf-8')
    except Exception as e:
        return "[Error de desencriptado]"