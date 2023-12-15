from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
import json
# Create your views here.
with open('country-by-languages.json') as countries_file:
    countries_list = json.load(countries_file)

languages_dict = {}
for country in countries_list:
    for language in country["languages"]:
        if language in languages_dict:
            languages_dict[language].append(country["country"])
        else:
            languages_dict[language] = []
            languages_dict[language].append(country["country"])

languages_list = []
for item in languages_dict:
    languages_list.append({"language": item, "countries": languages_dict[item]})


def main(request):
    return HttpResponse(f'<h1>Приветствую!</h1>'
                        f'<a href=countries-list>Страны</a>&nbsp'
                        f'<a href=languages-list>Языки</a>'
                       )


def countries(request):
    paginator = Paginator(countries_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'countries-list.html', {'page_obj': page_obj})


def country(request, requested_country):
    return render(request, 'country.html', {'countries': countries_list, 'requested_country': requested_country})


def letter(request, letter):
    return render(request, 'countries-list-by-letter.html', {'countries': countries_list, 'letter': letter})


def languages(request):
    return render(request, 'languages-list.html', {'languages_list': languages_list})


def language(request, requested_language):
    print(requested_language)
    return render(request, 'countries-list-by-language.html', {'languages_list': languages_list, 'requested_language': requested_language})