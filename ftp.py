import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from settings import STORAGE_DIR


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous('.')

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('0.0.0.0', 21)
    server = FTPServer(address, handler)

    server.serve_forever()


if __name__ == "__main__":
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    os.chdir(STORAGE_DIR)
    main()
