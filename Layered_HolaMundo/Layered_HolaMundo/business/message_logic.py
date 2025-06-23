from data.message_repository import get_message_from_db

def build_message():
    # Podrías agregar reglas de negocio aquí
    return get_message_from_db()
