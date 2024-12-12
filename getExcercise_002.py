import configuration  # para acceder a los archivos URL_SERVICE y DOC_PATH
import requests  # para poder hacer requests importamos la libreria Requests


# Envío de solicitud:
# Definimos la función get_docs()
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)
