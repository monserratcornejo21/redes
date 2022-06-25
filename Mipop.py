# importamos funciones socket 
import socket

def EstablecerConexion(user, passwd):
    host = "192.168.1.86"
    port = 110
    ipv4 = socket.AF_INET
    tcp  = socket.SOCK_STREAM
   
    conexion = socket.socket(ipv4, tcp)
    conexion.connect((host, port))
    respuesta = conexion.recv(1024).decode()
    comando = "USER {}\n".format(user)
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    comando = "PASS {}\n".format(passwd)
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    return (conexion)
    
#establecemos una funcion y variables 
def listar_correo(user, passwd):
    
    conexion=EstablecerConexion(user,passwd)
    # funcion USER en el cual el cliente ingresara su dato de usuario en sistema
    #print(respuesta)

    # funcion PASS en el cual el cliente ingresara su dato de usuario en sistema
    #print(respuesta)

    #funcion LIST con la cual el cliente obtendra la lista de correos disponibles en servidor
    comando = "LIST\n"
    #print(comando)
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    SalirDelPop(conexion)
    return(respuesta)


#establecemos una funcion 
def operaciones(opcion,numero_email,user,passwd):
    #al cliente le daremos 3 opciones por pantalla, con las cuales podra ver o eliminar un mensaje; ademas de salir de la lista 
    conexion=EstablecerConexion(user, passwd)
    while True:
        if (opcion =="1"):
            #para ver uno de los mensajes especifico listados
            comando = "RETR {}\n".format(numero_email)
            print(comando)
            conexion.send(comando.encode())
            respuesta = conexion.recv(1024).decode()
            SalirDelPop(conexion)
            return(respuesta)

        elif (opcion =="2"):
            #para borrar un email especifico
            comando = "DELE {}\n".format(numero_email)
            print(comando)
            conexion.send(comando.encode())
            respuesta = conexion.recv(1024).decode()
            print(respuesta)
            SalirDelPop(conexion)
            return(respuesta)

# funcion que sirve para que el cliente salga del programa de mensajeria
def SalirDelPop(conexion):
    comando = "QUIT\n"
    conexion.send(comando.encode())
    respuesta = conexion.recv(1024).decode()
    return(respuesta,"ADIOS.")
