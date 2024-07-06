from API.response_model import ResourceRequestResponse, ResourceRequest


def test_get_resource_requests(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    ResourceRequestResponse(tasks=response.json())
    print(response.json())


def test_get_resource_requests_invalid_project_id(client):
    client.set_project_id(1111111)
    response = client.get_projects_resource_requests()
    assert response.status_code == 404


def test_get_resource_requests_id(client, resource_request_id):
    response = client.get_projects_resource_request_by_id(resource_request_id)
    assert response.status_code == 200
    ResourceRequest(**response.json())


def test_get_resource_requests_invalid_id(client):
    response = client.get_projects_resource_request_by_id(111)
    assert response.status_code == 404


def test_get_resource_requests_company_id(client):
    response = client.get_companies_resource_request()
    assert response.status_code == 200
    ResourceRequestResponse(tasks=response.json())


def test_get_resource_requests_length_id(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    ResourceRequestResponse(tasks=response.json())
    for item in response.json():
        assert len(str(item['id'])) >= 5


def test_get_resource_requests_boolean_id(client):
    response = client.get_projects_resource_request_by_id(False)
    assert response.status_code == 404


def test_get_resource_requests_string_id(client):
    response = client.get_projects_resource_request_by_id('number')
    assert response.status_code == 404


def test_get_resource_requests_negative_id(client):
    response = client.get_projects_resource_request_by_id(-111)
    assert response.status_code == 404


def test_get_resource_requests_floating_id(client):
    response = client.get_projects_resource_request_by_id(111.111)
    assert response.status_code == 404
