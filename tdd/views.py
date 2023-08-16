from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def get_cite(request, city):
    with open("tdd\db.json") as json_file:
        data = json.load(json_file)
        for city_data in data["cities"]:
            if city_data["name"] == city:
                return JsonResponse(city_data)
        return JsonResponse({"msg": "data not found!"})

def create_data(request, city):
    with open("tdd\db.json") as json_file:
        data = json.load(json_file)
        for city_data in data["cities"]:
            if city_data["name"] == city:
                return JsonResponse(city_data)
        return JsonResponse({"msg": "data not found!"})
