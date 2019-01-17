import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from settings import STORAGE_DIR


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('127.0.0.1', 21)
    server = FTPServer(address, handler)

    server.serve_forever()


if __name__ == "__main__":
    os.chdir(STORAGE_DIR)
    main()
