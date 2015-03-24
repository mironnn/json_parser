from django.shortcuts import render, render_to_response, redirect
from json_app.models import Region, City
from django.http import HttpResponse
import json
from .forms import form_file

# Create your views here.


def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)


def open_file(request):
    if 'form_object' in request.FILES:
        form = form_file(request.POST, request.FILES)
        object = request.FILES['form_object']
        json_object = json.load(object)
        regions_k = json_object.keys()
        for region_k in regions_k:
            temp_region = Region()
            temp_region.name = region_k
            temp_region.save()
            region_cities_kv = json_object[region_k]
            region_cities_k = region_cities_kv.keys()
            for region_city_k in region_cities_k:
                temp_city = City()
                temp_city.region_id = Region()
                temp_city.name = region_city_k
                temp_city.area = float(region_cities_kv[region_city_k])
                temp_city.region_id_id = int(temp_region.id)
                temp_city.save()
        template = "index.html"
        all_cities = City.objects.all()
        # json_all_cities = json.dumps(all_cities)
        context = {'form': form, 'all_cities': all_cities, 'json_all_cities': '''json_all_cities'''}
        return render(request, template, context)