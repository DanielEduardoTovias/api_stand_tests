import configuration  # para acceder a los archivos URL_SERVICE y DOC_PATH
import requests  # para poder hacer requests importamos la libreria Requests


# Envío de solicitud:
# Definimos la función get_docs()
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


# Guardamos la respuesta en la variable response:
response = get_docs()  # Llamamos a la función get_docs() y se realiza una solicitud GET a la combinación: URL_SERVICE y DOC_PATH

# Imprimimos el codigo de respuesta de la petition:
print(response.status_code)
