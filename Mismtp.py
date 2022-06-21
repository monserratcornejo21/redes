#importamos funciones socket
import socket

#establecemos una funcion para manejar la cantidad de bits que tendra el mensaje, transformacion de 16 a 8 y viceversa
def enviar(conexion,men):
    msg = men + '\n'
    conexion.send(msg.encode())

def recibir(conexion):
    msg = conexion.recv(1024)
    print(msg.decode())
#establecemos variables

host = "taller2.localhost"
port = 25
ipv4 = socket.AF_INET
tcp  = socket.SOCK_STREAM
user = input

# con datos entregados por la estructura TCP y ipv4, a la direccion de coneccion le damos un orden de ejecucion segun datos ingresados por usuario 
with socket.socket(ipv4,tcp) as conexion:

    conexion.connect((host, port))
    recibir(conexion)
    enviar(conexion,'HELLO')
    recibir(conexion)
    enviar(conexion,'MAIL FROM: {}'.format(host))
    recibir(conexion)
    enviar(conexion,'RCPT TO: {}'.format(user))
    recibir(conexion)
    enviar(conexion,'DATA')
    recibir(conexion)
    enviar(conexion,'Subject: muestra script en python')
    enviar(conexion,'From:',host)
    enviar(conexion,'To: ',user)
    enviar(conexion,'')
    enviar(conexion,'muestra en python')
    enviar(conexion,'cualquier cosa como mensaje......')
    enviar(conexion,'es un ejemplo......')
    enviar(conexion,'')
    enviar(conexion,'.')
    recibir(conexion)
    enviar(conexion,'quit')