import pytest
import uuid
import json
from unittest.mock import patch

from api import app, AsyncResult


client = app.test_client()


@pytest.mark.celery(result_backend='amqp://')
def test_text():
    payload = {'site': 'http://example.com'}
    response = client.post('/text', data=payload)

    assert response._status_code == 200

    response_payload = json.loads(response.data.decode('utf-8'))
    assert 'task_id' in response_payload


@pytest.mark.celery(result_backend='amqp://')
def test_images():
    payload = {'site': 'http://example.com'}
    response = client.post('/images', data=payload)

    assert response._status_code == 200

    response_payload = json.loads(response.data.decode('utf-8'))
    assert 'task_id' in response_payload


def test_status():
    task_id = uuid.uuid4()
    status = 'PENDING'
    with patch.object(AsyncResult, 'status', status) as mocked_status:
        response = client.get('/status/{}'.format(task_id))

    assert response._status_code == 200

    response_payload = json.loads(response.data.decode('utf-8'))
    assert response_payload == {'status': status}