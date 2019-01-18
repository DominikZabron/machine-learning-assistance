# Machine learning assistant

## Installation

## Using Docker

    $ docker-compose build && docker-compose up
    
## Local installation

### Install rabbitmq (MacOS)

    $ brew install rabbitmq

### Add rabbitmq to path:

    $ PATH=$PATH:/usr/local/sbin
    
### Install pipenv

    $ pip install pipenv
    
### Install dependencies

    $ pipenv install

### Run rabbitmq

    $ rabbitmq-server -detached

### Start celery

    $ celery -A tasks worker --loglevel=info

### Run FTP Server

    $ python ftp.py
    
### Run App

    $ python api.py
    
## Basic Usage

### Request fetching website text content

    $ curl -d "site=http://google.com" 127.0.0.1:5000/text
    $ > {"task_id": "4373403a-56b5-4b3a-ace2-579526bd056c"}
    
### Request fetching website images

    $ curl -d "site=http://google.com" 127.0.0.1:5000/images
    $ > {"task_id": "46e34179-7758-4ad8-b81f-3f53951fb749"}
    
### Check task status
    
    $ curl 127.0.0.1:5000/status/46e34179-7758-4ad8-b81f-3f53951fb749
    $ > {"status": "SUCCESS"}
    
### Download assets via FTP:

    ftp://127.0.0.1