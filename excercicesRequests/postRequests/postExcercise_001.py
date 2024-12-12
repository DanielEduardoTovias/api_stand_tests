import configuration  # para acceder a los archivos URL_SERVICE y DOC_PATH
import requests  # para poder hacer requests importamos la libreria Requests
import data


# Envío de solicitud: para crear nuevos usuarios con el método POST
# Definimos la función post_new_user
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # inserta el cuerpo de solicitud
                         json=products_ids,
                         headers=data.headers)  # inserta los encabezados


response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.headers)
print(response.url)
print(response.headers['Date'])
print(type(response.json()))
print(response.json())

