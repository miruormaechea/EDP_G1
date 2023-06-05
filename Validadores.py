import string


def solo_letras(str):
    lista=list(char in string.ascii_letters  for char in str)
    if False in lista:
        return False
    else:
        return True


def verMail(mail):
    sintaxis1=['gmail','yahoo','hotmail']
    sintaxis2=['.com','.ar','.net']


    if mail.find('@')<1:
        return False
    else:
        indice1=''
        cont1=0
        for i in sintaxis1:
            if mail.find(i)!=-1:
                indice1=mail.find(i)
                long_sintaxis1=len(i)
                cont1+=1
        if cont1!=1 or indice1!=mail.find('@')+1:
            return False
        else:
            indice2=''
            cont2=0
            for i in sintaxis2:
                if mail.find(i)!=-1:
                    indice2=mail.find(i)
                    cont2+=1
            if cont2!=1 or indice2!=indice1+long_sintaxis1:
                  return False
            else:
                return True




def verTelefono(telefono):
    for i in range(len(telefono)):
        if (not telefono.isnumeric()) or len(telefono) < 7:
            return False
        else:
            return True




def verDNI(DNI):
    if (not DNI.isnumeric()) or int(DNI) > 99999999 or int(DNI) < 1000000:
        return False
    else:
        return True


def verNombre(nombre): #se usa para el nombre y el apellido
    if solo_letras(nombre)==False or len(nombre) < 2 or len(nombre) > 35:
        return False
    else:
        return True


def verAltura(altura):
    if (not altura.isnumeric()) or int (altura) > 25000 or int (altura) < 100:
        return False
    else:
        return True


def es_int(valor:str):
    if valor.isnumeric():
        return True
    else:
        return False

#comentario
def verificar_rango(valor, n):
    if es_int(valor):
        return int(valor)>0 and int(valor)<=n
    else:
        return False



