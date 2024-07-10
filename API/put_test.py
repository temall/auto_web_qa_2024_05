from API.response_model import ResourceRequest
import pytest
from datetime import datetime


@pytest.mark.parametrize("cost, volume",
                         [(44, 456)],
                         ids=["cost_changed, volume_changed"])
def test_put_resource_requests_successfully_changed_values(client, resource_requests, cost, volume):
    data = {"volume": volume,
            "cost": cost}
    response = client.put_projects_resource_requests(resource_request_id=resource_requests, data=data)
    assert response.status_code == 200
    ResourceRequest(**response.json())
    assert response.json()['cost'] == cost
    assert response.json()['volume'] == volume


def test_put_resource_requests_change_needed_at(client, resource_requests):
    data = {
        "needed_at": int(datetime.now().timestamp() + 1000)
    }
    response = client.put_projects_resource_requests(resource_request_id=resource_requests, data=data)
    assert response.status_code == 200
    ResourceRequest(**response.json())


@pytest.mark.parametrize("order_status, status_code",
                         [(10, 400), (20, 400)],
                         ids=["draft", "waiting for payment"])
def test_put_resource_requests_included_in_order_in_status_draft(client, resource_requests, order_status, status_code):
    contractor_id = client.get_companies_contractors().json()[0]['id']
    stock_id = client.get_companies_stocks().json()[0]['id']
    data_orders = {
        "contractor_id": contractor_id,
        "pay_until_date": int(datetime.now().timestamp()),
        "status": order_status,
        "items": [{
            "resource_request_id": resource_requests,
            "volume": 33,
            "cost": 123
        }],
        "stock_id": stock_id
    }
    created_order_id = client.post_projects_orders(data_orders).json()['id']

    data = {
        "needed_at": int(datetime.now().timestamp())
    }
    response = client.put_projects_resource_requests(resource_request_id=resource_requests, data=data)
    deleted_order = client.delete_companies_orders(created_order_id)
    assert deleted_order.status_code == 204
    assert response.status_code == status_code, (f"Expected {status_code}, got {response.status_code} with response"
                                                 f" {response.content}")


def test_put_resource_requests_not_over_budget(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 33,
        "cost": 123,
        "is_over_budget": False,
        "needed_at": int(datetime.now().timestamp())
    }

    response = client.post_projects_resource_requests(data=data)
    assert response.status_code == 201
    data = {
        "cost": 123,
        "is_over_budget": True,
    }
    new_resource_request_id = response.json()['id']
    response_put = client.put_projects_resource_requests(data=data, resource_request_id=new_resource_request_id)
    assert response_put.status_code == 400
