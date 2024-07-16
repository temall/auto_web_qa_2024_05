from datetime import datetime
import pytest


def test_delete_resource_requests_successful(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 33,
        "cost": 123,
        "is_over_budget": True,
        "needed_at": int(datetime.now().timestamp())
    }
    response = client.post_projects_resource_requests(data)
    assert response.status_code == 201
    new_resource_request_id = response.json()['id']
    response_delete = client.delete_projects_resource_requests(new_resource_request_id)
    assert response_delete.status_code == 204


def test_delete_resource_requests_over_budget_false(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 33,
        "cost": 123,
        "is_over_budget": True,
        "needed_at": int(datetime.now().timestamp())
    }
    response = client.post_projects_resource_requests(data)
    assert response.status_code == 201
    new_resource_request_id = response.json()['id']
    response_delete = client.delete_projects_resource_requests(new_resource_request_id)
    assert response_delete.status_code == 422


@pytest.mark.parametrize('resource_requests',
                         [111111, -111111, False],
                         ids=['non-existent', 'negative', 'boolean'])
def test_delete_nonexistent_resource_requests(client, resource_requests):
    response = client.delete_projects_resource_requests(resource_requests)
    assert response.status_code == 404
    assert response.json()['name'] == "Not Found"
