# Protocolo-FTP
Trabajo Práctico N°7 - Redes de Datos

## Integrantes

| Integrante |
|---|
| Leonardo Gonzalez |
| Alexandra Fernandez |
| Daniela Illanes |
| Julieta Paoloni |
| Santiago Cucchiarelli |

# Cliente FTP

Cliente FTP en Python con menú por consola. 

## Funcionalidades

| Opción | Acción | Comando FTP |
|---|---|---|
| 1 | Listar archivos del servidor | `LIST` |
| 2 | Cambiar de carpeta | `CWD` |
| 3 | Mostrar carpeta actual | `PWD` |
| 4 | Descargar un archivo | `RETR` |
| 5 | Subir un archivo | `STOR` |
| 6 | Crear carpeta | `MKD` |
| 7 | Borrar archivo | `DELE` |
| 8 | Borrar carpeta | `RMD` |
| 9 | Renombrar | `RNFR` / `RNTO` |
| 0 | Salir | `QUIT` |

Al conectarse también se usan `USER` y `PASS` (autenticación) y `PASV` (modo pasivo para el canal de datos), que `ftplib` maneja internamente.

## Requisitos

- Python 3.8 o superior
- Para probar con el servidor local: `pip install pyftpdlib`

## Uso

### 1. Levantar un servidor de prueba

En la carpeta que queremos compartir:

```
python servidor.py
```

Queda escuchando en el puerto 2121 con estos usuarios:

- `usuario` / `1234`: permisos completos (subir, bajar, borrar, etc.)
- `anonymous` (sin contraseña): solo lectura

También se puede levantar rápido, sin script, con acceso anónimo y escritura:

```
python -m pyftpdlib -p 2121 -w
```

### 2. Ejecutar el cliente

```
python cliente_ftp.py
```

Ejemplo de datos para conectarse al servidor local:

```
Servidor: localhost
Puerto (21): 2121
Usuario (anonymous): usuario
Contraseña: 1234
```

## Estructura

```
cliente_ftp.py   # cliente FTP con menú
servidor.py      # servidor FTP local de prueba
README.md
```

## Capturas
## Capturas

### 1. Cliente: conexión y autenticación

Cliente conectado

<img width="595" height="280" alt="image" src="https://github.com/user-attachments/assets/097c283d-d759-4b52-85a3-51419fe778b8" />


El cliente se conecta al servidor local (`localhost`, puerto `2121`) con el usuario `anonymous`. El servidor responde `220 pyftpdlib 2.2.0 ready.` (servidor listo) y `230 Login successful.` (autenticación correcta). A continuación se muestra el menú con las operaciones disponibles.

### 2. Servidor: registro de la sesión

Log del servidor

<img width="634" height="126" alt="image" src="https://github.com/user-attachments/assets/0b2db2e0-a2f7-420c-96db-2f7a0826136d" />


Registro del servidor `pyftpdlib` durante la prueba:

- `starting FTP server on 0.0.0.0:2121`: el servidor queda escuchando en el puerto 2121.
- `FTP session opened (connect)`: el cliente abre la conexión de control desde `127.0.0.1`.
- `USER 'anonymous' logged in`: el usuario se autentica correctamente.
- `MKD C:\ftp_prueba\prueba_protocolo 257`: el cliente crea una carpeta remota con el comando `MKD` y el servidor responde con el código `257` (directorio creado).
- `Control connection timed out` / `FTP session closed`: la sesión se cierra automáticamente tras un período de inactividad.
>


