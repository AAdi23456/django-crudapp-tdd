from django.urls import reverse
import json


def test_get_route(client):
    expected_temperatures = {
        "New York": 72,
        "Los Angeles": 85,
        "Madhubani": 65,
        "patna": 89,
    }
    for city_name, expected_temperature in expected_temperatures.items():
        response = client.get(reverse("temprature"), {"city": city_name})
        assert response.status_code == 200
        expected_data = {"name": city_name, "temprature": expected_temperature}
        assert response.json() == expected_data
