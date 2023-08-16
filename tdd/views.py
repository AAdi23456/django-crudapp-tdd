from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

# Read city information
def get_city(request, city):
    with open("tdd\db.json") as json_file:
        data = json.load(json_file)
        for city_data in data["cities"]:
            if city_data["name"] == city:
                return JsonResponse(city_data)
        return JsonResponse({"msg": "City not found!"}, status=404)

# Create a new city
@csrf_exempt
@require_POST
def create_city(request):
    data = json.loads(request.body)
    with open("tdd\db.json") as json_file:
        cities_data = json.load(json_file)
    
    new_city = {
        "name": data.get("name"),
        "temperature": data.get("temperature")
    }
    
    cities_data["cities"].append(new_city)
    
    with open("tdd\db.json", "w") as json_file:
        json.dump(cities_data, json_file, indent=4)
    
    return JsonResponse(new_city, status=201)

# Update city information
@csrf_exempt
@require_POST
def update_city(request, city):
    data = json.loads(request.body)
    with open("tdd\db.json") as json_file:
        cities_data = json.load(json_file)
    
    for city_data in cities_data["cities"]:
        if city_data["name"] == city:
            city_data["temperature"] = data.get("temperature")
            with open("tdd\db.json", "w") as json_file:
                json.dump(cities_data, json_file, indent=4)
            return JsonResponse(city_data)
    
    return JsonResponse({"msg": "City not found!"}, status=404)

# Delete city
@csrf_exempt
def delete_city(request, city):
    with open("tdd\db.json") as json_file:
        cities_data = json.load(json_file)
    
    for i, city_data in enumerate(cities_data["cities"]):
        if city_data["name"] == city:
            deleted_city = cities_data["cities"].pop(i)
            with open("tdd\db.json", "w") as json_file:
                json.dump(cities_data, json_file, indent=4)
            return JsonResponse(deleted_city)
    
    return JsonResponse({"msg": "City not found!"}, status=404)
