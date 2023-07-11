from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from .t_code import database_conn as db

def index_page(request):
    persons = db.get_all_persons()
    paginator = Paginator(persons, 5)  # Podeli objekte na stranice sa po 10 elemenata
    page_number = request.GET.get('page')  # Preuzmi broj trenutne stranice iz zahteva
    page_obj = paginator.get_page(page_number) 
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def person_details(request, parametar):
    print(parametar)
    chosen_person = db.find_person_by_ID(int(parametar))
    context = {'person': chosen_person}
    return render(request, 'person_details.html', context)
