# importamos funciones socket 
import socket

#establecemos una funcion y variables 
def listar_correo(user, passwd):

    host = '192.168.0.24'
    port = 110
    ipv4 = socket.AF_INET
    tcp  = socket.SOCK_STREAM

    conexion = socket.socket(ipv4, tcp)
    conexion.connect((host, port))
    respuesta = conexion.recv(1024).decode()
    #print(respuesta)

    # funcion USER en el cual el cliente ingresara su dato de usuario en sistema
    comando = "USER {}\n".format(user)
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    #print(respuesta)

    # funcion PASS en el cual el cliente ingresara su dato de usuario en sistema
    comando = "PASS {}\n".format(passwd)
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    #print(respuesta)

    #funcion LIST con la cual el cliente obtendra la lista de correos disponibles en servidor
    comando = "LIST\n"
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    return(respuesta)

#establecemos una funcion 
def operaciones(opcion,numero_email):
    #al cliente le daremos 3 opciones por pantalla, con las cuales podra ver o eliminar un mensaje; ademas de salir de la lista 
    while True:

        if (opcion =="1"):
            #para ver uno de los mensajes especifico listados
            comando = "RETR {}\n".format(numero_email)
            conexion.send(comando.encode())
            respuesta = conexion.recv(1024).decode()
            return(respuesta)

        elif (opcion =="2"):
            #para borrar un email especifico
            comando = "DELET {}\n".format(numero_email)
            conexion.send(comando.encode())
            respuesta = conexion.recv(1024).decode()
            return(respuesta)

        elif (opcion =="3"):
            comando = "QUIT\n"
            conexion.send(comando.encode())
            respuesta = conexion.recv(1024).decode()
            return(respuesta)
        else:
            return("Opcion Invalida")

# funcion que sirve para que el cliente salga del programa de mensajeria
def SalirDelPop():
    comando = "QUIT\n"
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    return(respuesta,"ADIOS.")