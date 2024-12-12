import getExcercise_002
import sender_stand_request_post
import data

#Preparando los datos para la prueba:

def get_user_body(first_name):
    #Tomamos el diccionario y hacemos una copia para no modificar los datos del diccionario orginal
    current_body = data.user_body.copy()
    #Cambiamos el valor del campo "firstName"
    current_body["firstName"] = first_name
    #Develvemos un nuevo diccionario con el campo "firstName" modificado
    return current_body


# Función de prueba positiva:
def possitive_assert(first_name):
    user_body = get_user_body(first_name) #Guardamos el cuerpo(diccionario) modificado de la solicitud en la variable: user_body
    user_response = sender_stand_request_post.post_new_user(user_body) #resultado de la solicitud para crear nuevo usuari@ en la variable: user_response
    #Comprobar si la respiuesta tiene el codigo: 201
    assert user_response.status_code == 201
    #Comprobar que la respuesta contenga el campo: "authToken" y que contenga algunos datos
    assert user_response.json()["authToken"] != ""
    print(user_response)

    # comprobar si hay un registro de creación de un nuevo usuario o usuaria guardado en la tabla users.
    #resultado de "user_model" se guarda en "user_table_response"
    users_table_response = getExcercise_002.get_users_table()
    # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


#Función de prueba negatva:
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)  # Guardamos el cuerpo(diccionario) modificado de la solicitud en la variable: user_body
    #comprobar si la var. "response" almacena el resultado de la solicitud
    user_response = sender_stand_request_post.post_new_user(user_body)  # resultado de la solicitud para crear nuevo usuari@ en la variable: user_response
    assert user_response.status_code == 400     # Comprobar si la respiuesta tiene el codigo: 400
    assert user_response.json()["code"] == 400  #Comprobar si el atributo "code" == 400
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."
    print(user_response.status_code)


#Función de prueba negatva sin el atributo "firstName":
def negative_assert_no_first_name(user_body):
    response = sender_stand_request_post.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    #assert response.json()["message"] == "No se enviaron todos los parámetros necesarios"

'''Has introducido un nombre de usuario no válido. El nombre solo puede '
 'contener letras del alfabeto latino, la longitud debe ser de 2 a 15 '
 'caracteres.'''


#Automatización de las pruebas:

# Prueba 1. Creación de un nuevo usuari@  [Ver lista de comprobación]
# El parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    possitive_assert("Aa")

#Prueba 2.
def test_create_user_15_letter_in_first_name_get_success_response():
    possitive_assert("Aaaaaaaaaaaaaaa")

#Prueba 3.
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")


#Prueba 4.
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")


#Prueba 5.
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")


#Prueba 6.
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")


#Prueba 7.
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


#Prueba 8.
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy() #HAcemos copia del diccionario
    user_body.pop("firstName") #eliminamos el atributo "firstName" de la copia del diccionario
    #llamamos la función para comprobar la respuesta
    negative_assert_no_first_name(user_body) 


#Prueba 9.
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)


#Prueba 10.
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    negative_assert_no_first_name(user_body)


