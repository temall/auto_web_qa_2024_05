from API.response_model import ResourceRequest
import pytest
from datetime import datetime


def test_successful_post_resource_requests(client, resource):
    data = {"project_tasks_resource_id": resource,
            'volume': 33,
            'cost': 123,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 201
    ResourceRequest(**response.json())


def test_post_resource_requests_with_missing_required_field(client, resource):
    data = {"project_tasks_resource_id": resource,
            'cost': 123,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


@pytest.mark.parametrize("project_tasks_resource_id",
                         [(-111), 0, 111.111, False],
                         ids=['negative', 'zero', 'boolean', 'logical'])
def test_post_resource_requests_invalid_id(client, project_tasks_resource_id):
    data = {"project_tasks_resource_id": project_tasks_resource_id,
            'volume': 33,
            'cost': 123,
            "is_over_budget": False,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


@pytest.mark.parametrize("volume, cost",
                         [(-33, 123), (33, -123), (True, False)],
                         ids=['negative_cost', 'negative_volume', 'boolean'])
def test_post_resource_requests_invalid_values(client, resource, volume, cost):
    data = {"project_tasks_resource_id": resource,
            'volume': volume,
            'cost': cost,
            "is_over_budget": False,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


def test_post_resource_requests_with_false_data_validation(client, resource):
    data = {"project_tasks_resource_id": resource,
            'volume': 33,
            'cost': 111,
            "is_over_budget": 'over_budget',
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422
