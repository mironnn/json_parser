from django.shortcuts import render, render_to_response, redirect
from json_app.models import Region, City
from django.http import HttpResponse
import json
from .forms import form_file

# Create your views here.


def index(request):
    regions = Region.objects.all()
    context = {'regions': regions}
    template = "index.html"
    return render(request, template, context)


def json_template(request):
    context = {}
    template = "json_template.html"
    return render(request, template, context)


def open_file(request):
    if 'form_object' in request.FILES:
        form = form_file(request.POST, request.FILES)
        object = request.FILES['form_object']
        json_object = json.load(object)
        regions_k = json_object.keys()
        for region_k in regions_k:
            temp_region = Region()
            t = Region.objects.filter(name=region_k).first()
            if t == None:
                t = Region()
            if t.name != region_k:
                temp_region.name = region_k
                temp_region.save()
                region_cities_kv = json_object[region_k]
                region_cities_k = region_cities_kv.keys()
                for region_city_k in region_cities_k:
                    temp_city = City()
                    temp_city.region_id = Region()
                    c = City.objects.filter(name=region_city_k).first()
                    if c == None:
                        c = City()
                    if c.name != region_city_k:
                        temp_city.name = region_city_k
                        temp_city.area = float(region_cities_kv[region_city_k])
                        temp_city.region_id_id = int(temp_region.id)
                        temp_city.save()
            else:
                region_cities_kv = json_object[region_k]
                region_cities_k = region_cities_kv.keys()
                for region_city_k in region_cities_k:
                    temp_city = City()
                    temp_city.region_id = Region()
                    c = City.objects.filter(name=region_city_k).first()
                    if c == None:
                        c = City()
                    if c.name != region_city_k:
                        temp_city.name = region_city_k
                        temp_city.area = float(region_cities_kv[region_city_k])
                        temp_city.region_id_id = int(t.id)
                        temp_city.save()
        template = "index.html"
        regions = Region.objects.all()
        context = {'form': form, 'regions': regions}

        return render(request, template, context)


def load_chart(request):
    cities = City.objects.filter(region_id=request.GET['region'])
    cities_list_temp = [city.as_dict()
                        for city in cities]
    cities_list = sorted (cities_list_temp, reverse=True)
    cities_json = json.dumps(cities_list)

    return HttpResponse(cities_json,
                        content_type="application/json")

