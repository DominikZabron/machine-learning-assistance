# Machine learning assistant

## Installation

## Using Docker

    $ docker-compose build && docker-compose up
    
## Local installation

### Install rabbitmq

    $ brew install rabbitmq

### Add rabbitmq to path:

    $ PATH=$PATH:/usr/local/sbin

### Run rabbitmq

    $ rabbitmq-server -detached

### Start celery

    $ celery -A tasks worker --loglevel=info

### Run FTP Server

    $ sudo python ftp.py