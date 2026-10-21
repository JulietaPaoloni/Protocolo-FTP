"""
Cliente FTP con menú de comandos.
Redes de Datos - Implementación de un cliente FTP.

Permite conectarse a un servidor FTP, navegar, listar, subir y bajar
archivos, y administrar carpetas y archivos remotos.
"""
from ftplib import FTP, all_errors
import os

ftp = FTP()


def conectar():
    host = input("Servidor: ")
    puerto = int(input("Puerto (21): ") or 21)
    usuario = input("Usuario (anonymous): ") or "anonymous"
    clave = input("Contraseña: ")
    print(ftp.connect(host, puerto))
    print(ftp.login(usuario, clave))


def listar():
    ftp.retrlines("LIST")


def descargar():
    nombre = input("Archivo remoto: ")
    with open(nombre, "wb") as f:
        ftp.retrbinary(f"RETR {nombre}", f.write)
    print("Descargado:", nombre)


def subir():
    ruta = input("Archivo local: ")
    if not os.path.isfile(ruta):
        print("No existe el archivo local:", ruta)
        return
    with open(ruta, "rb") as f:
        ftp.storbinary(f"STOR {os.path.basename(ruta)}", f)
    print("Subido:", ruta)


def menu():
    print("""
1. Listar          2. Cambiar carpeta   3. Carpeta actual
4. Descargar       5. Subir             6. Crear carpeta
7. Borrar archivo  8. Borrar carpeta    9. Renombrar
0. Salir""")


acciones = {
    "1": listar,
    "2": lambda: print(ftp.cwd(input("Carpeta: "))),
    "3": lambda: print(ftp.pwd()),
    "4": descargar,
    "5": subir,
    "6": lambda: print(ftp.mkd(input("Nombre: "))),
    "7": lambda: print(ftp.delete(input("Archivo: "))),
    "8": lambda: print(ftp.rmd(input("Carpeta: "))),
    "9": lambda: print(ftp.rename(input("Nombre actual: "), input("Nombre nuevo: "))),
}


def main():
    try:
        conectar()
        while True:
            menu()
            op = input("> ")
            if op == "0":
                break
            try:
                acciones.get(op, lambda: print("Opción inválida"))()
            except all_errors as e:
                print("Error:", e)
    except all_errors as e:
        print("No se pudo conectar:", e)
    except OSError as e:
        print("Error de conexión:", e)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass


if __name__ == "__main__":
    main()
