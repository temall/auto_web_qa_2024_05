from API.http_client import GectaroHttpClient
from API.response_model import ResourceRequest
from datetime import datetime
import pytest


def pytest_addoption(parser):
    parser.addoption("--token")
    parser.addoption("--url", default="https://api.gectaro.com")


@pytest.fixture(scope='session')
def token(request):
    return request.config.getoption('--token')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def client(token, base_url):
    client = GectaroHttpClient(base_url=base_url,
                               token=token)
    yield client


@pytest.fixture()
def resource(client):
    data = {
        'name': "Resource Name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": client.project_id,
        'type': 1,
        'volume': 33
    }
    resource_response = client.post_projects_resource(data)
    assert resource_response.status_code == 201
    resource_id = resource_response.json()['id']
    yield resource_id
    resource_delete_response = client.delete_projects_resource(resource_id)
    assert resource_delete_response.status_code == 204, f"Resource {resource_id} doesnt deleted"


@pytest.fixture()
def resource_requests_id(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    yield response.json()[0]['id']


@pytest.fixture()
def resource_requests(resource, client):
    data = {"project_tasks_resource_id": resource,
            'volume': 33,
            'cost': 123,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_requests(data=data)
    assert response.status_code == 201
    ResourceRequest(**response.json())
    new_resource_request_id = response.json()['id']
    yield new_resource_request_id
