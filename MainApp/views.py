from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
with open('country-by-languages.json') as countries_file:
    countries_list = json.load(countries_file)


def main(request):
    return HttpResponse(f'<h1>Приветствую!</h1>'
                        f'<a href=countries>Страны</a>')


def countries(request):
    return render(request, 'countries.html', {'countries':countries_list})



def country(request, requested_country):
    return render(request, 'country.html', {'countries':countries_list, 'requested_country':requested_country})


def page(request):
    return render(request, 'countries.html', {'countries':countries})


def letter(request):
    return render(request, 'countries.html', {'countries':countries})