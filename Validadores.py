import string


def solo_letras(str):
    """
    Verifica si una cadena contiene solo letras.
    :param str: La cadena a verificar.
    :return: True si la cadena contiene solo letras, False en caso contrario.
    """
    lista = list(char in string.ascii_letters for char in str)
    if False in lista:
        return False
    else:
        return True


def verMail(mail):
    """
    Verifica si una dirección de correo electrónico tiene una sintaxis válida.
    :param mail: La dirección de correo electrónico a verificar.
    :return: True si la dirección de correo electrónico tiene una sintaxis válida, False en caso contrario.
    """
    sintaxis1 = ['gmail', 'yahoo', 'hotmail']
    sintaxis2 = ['.com', '.ar', '.net']

    if mail.find('@') < 1:
        return False
    else:
        indice1 = ''
        cont1 = 0
        for i in sintaxis1:
            if mail.find(i) != -1:
                indice1 = mail.find(i)
                long_sintaxis1 = len(i)
                cont1 += 1
        if cont1 != 1 or indice1 != mail.find('@') + 1:
            return False
        else:
            indice2 = ''
            cont2 = 0
            for i in sintaxis2:
                if mail.find(i) != -1:
                    indice2 = mail.find(i)
                    cont2 += 1
            if cont2 != 1 or indice2 != indice1 + long_sintaxis1:
                return False
            else:
                return True


def verTelefono(telefono):
    """
    Verifica si un número de teléfono tiene un formato válido.
    :param telefono: El número de teléfono a verificar.
    :return: True si el número de teléfono tiene un formato válido, False en caso contrario.
    """
    for i in range(len(telefono)):
        if (not telefono.isnumeric()) or len(telefono) < 7:
            return False
        else:
            return True


def verDNI(DNI):
    """
    Verifica si un número de DNI tiene un formato válido.
    :param DNI: El número de DNI a verificar.
    :return: True si el número de DNI tiene un formato válido, False en caso contrario.
    """
    if (not DNI.isnumeric()) or int(DNI) > 99999999 or int(DNI) < 1000000:
        return False
    else:
        return True


def verNombre(nombre):  # se usa para el nombre y el apellido
    """
    Verifica si un nombre o apellido tiene un formato válido.
    :param nombre: El nombre o apellido a verificar.
    :return: True si el nombre o apellido tiene un formato válido, False en caso contrario.
    """
    if solo_letras(nombre) == False or len(nombre) < 2 or len(nombre) > 35:
        return False
    else:
        return True


def verAltura(altura):
    """
    Verifica si una altura tiene un formato válido.
    :param altura: La altura a verificar.
    :return: True si la altura tiene un formato válido, False en caso contrario.
    """
    if (not altura.isnumeric()) or int(altura) > 25000 or int(altura) < 100:
        return False
    else:
        return True


def es_int(valor: str):
    """
    Verifica si un valor es un entero.
    :param valor: El valor a verificar.
    :return: True si el valor es un entero, False en caso contrario.
    """
    if valor.isnumeric():
        return True
    else:
        return False


def verificar_rango(valor, n):
    """
    Verifica si un valor se encuentra en el rango válido.
    :param valor: El valor a verificar.
    :param n: El límite superior del rango.
    :return: True si el valor se encuentra en el rango válido, False en caso contrario.
    """
    if es_int(valor):
        return int(valor) > 0 and int(valor) <= n
    else:
        return False
