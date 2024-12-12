import configuration  # para acceder a los archivos URL_SERVICE y DOC_PATH
import requests  # para poder hacer requests importamos la libreria Requests
import data


# Envío de solicitud: para crear nuevos usuarios con el método POST
# Definimos la función post_new_user
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())



