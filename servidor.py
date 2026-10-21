"""
Servidor FTP local de prueba (pyftpdlib).
Compartí la carpeta desde la que lo ejecutes.

Usuario con permisos completos: usuario / 1234
Usuario anónimo: solo lectura
"""
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

auth = DummyAuthorizer()
auth.add_user("usuario", "1234", ".", perm="elradfmw")  # permisos completos
auth.add_anonymous(".", perm="elr")                      # anónimo: solo lectura

handler = FTPHandler
handler.authorizer = auth

FTPServer(("0.0.0.0", 2121), handler).serve_forever()
