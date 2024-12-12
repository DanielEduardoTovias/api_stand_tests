import configuration  # para acceder a los archivos URL_SERVICE y DOC_PATH
import requests  # para poder hacer requests importamos la libreria Requests


# Envío de solicitud:
# Definimos la función get_docs()
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

response = get_logs()
print(response.status_code)
print(response.headers)