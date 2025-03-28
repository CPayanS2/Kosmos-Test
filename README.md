# Kosmos-Test

## Requerimientos principales
* Python 3.x
  
## Instalación / Configuración

* Clonar el repositorio en su máquina local
* Abrir una terminal para levantar el servidor en el directorio 'TCPServer' y ejecutar:
  * Windows:
    * python server.py
  * Linux:
    * python3 server.py
* Abrir al menos una terminal más en el directorio 'TCPServer' para los clientes y ejecutar:
  * Windows:
    * python client.py
  * Linux:
    * python3 client.py
* Se solicitará un nombre de usuario para identificar del lado del servidor al cliente que se está conectando y facilitar su entendimiento en los mensajes.

## Terminar procesos / Salir

* Cliente(s)
  * En la terminal de cada cliente enviar el siguiente mensaje al servidor: DESCONEXION
  * Cerrar terminal
* Servidor
  * Puede cerrar directamente la ventana de la terminal de ejecución o combiar CTRL + C.
