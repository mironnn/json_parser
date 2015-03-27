from django.shortcuts import render, render_to_response, redirect
from json_app.models import Region, City
from django.http import HttpResponse
import json
from .forms import form_file

# Create your views here.


def index(request):
    regions = Region.objects.all()
    context = {'regions':regions}
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
        all_regions= Region.objects.all()
                        # my_dict = {}
                        # l = int(len(all_cities ))
                        # for i in range(l):
                        #     c = City.objects.get(id=i)
                        #     temp_dict = c.as_dict()
                        #     my_dict[temp_dict['name']] = temp_dict['area']
                        # print(1111111111111111111)
                        # print(my_dict)
                        # json_all_cities = json.dumps(all_cities)
        context = {'form': form, 'all_regions': all_regions}
        return render(request, template, context)

# def load_chart(request):
#     regions = Region.objects.all()
#     regions_json = [region.as_dict()
#                         for region in regions]
#     response_data = {
#         'regions': regions_json
#     }
#
#     return HttpResponse(json.dumps(response_data),
#                         content_type="application/json")

def chart(request):
    if 'chart_region' in request.POST:
        print('1111')
        # chart_region_id = request.POST['region.id']
        cities = City.objects.filter(region_id=request.POST['chart_region'])
        cities_list = [city.as_dict()
                        for city in cities]
        # cities_dict = {
        #     'cities': cities_list
        # }

        cities_json = json.dumps(cities_list)
        regions = Region.objects.all()
        context = {'cities_json': cities_json, 'regions': regions, 'cities': cities}
        template = 'index.html'
        print(cities_json)
        print(type(cities_json))

        return render (request, template, context)