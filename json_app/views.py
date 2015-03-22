from django.shortcuts import render, render_to_response, redirect
from json_app.models import Region, City

# Create your views here.


def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)