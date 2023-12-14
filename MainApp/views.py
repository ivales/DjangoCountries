from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
import json
# Create your views here.
with open('country-by-languages.json') as countries_file:
    countries_list = json.load(countries_file)


def main(request):
    return HttpResponse(f'<h1>Приветствую!</h1>'
                        f'<a href=countries-list>Страны</a>')


def countries(request):
    paginator = Paginator(countries_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'countries-list.html', {'page_obj':page_obj})



def country(request, requested_country):
    return render(request, 'country.html', {'countries':countries_list, 'requested_country':requested_country})


def page(request):
    return render(request, 'countries-list.html', {'countries':countries})


def letter(request, letter):
    return render(request, 'countries-list-by-letter.html', {'countries':countries_list, 'letter': letter})


def languages(request):
    return render(request, 'languages.html', {'countries':countries_list})