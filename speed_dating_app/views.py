from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
import random
from .t_code import database_conn as db

def index_page(request):
    persons = db.get_all_persons()[:20]
    random.shuffle(persons)
    context = {'persons': persons}
    return render(request, 'index.html', context)

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def person_details(request, parametar):
    print(parametar)
    chosen_person = db.find_person_by_ID(int(parametar))
    context = {'person': chosen_person}
    return render(request, 'person_details.html', context)
