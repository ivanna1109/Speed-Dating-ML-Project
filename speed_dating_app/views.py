from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .t_code import database_conn as db

def index_page(request):
    persons = db.get_all_persons()[:10]
    context = {'persons': persons}
    return render(request, 'index.html', context)

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def person_details(request, personId):
    chosen_person = db.get_all_persons()[:10]
    context = {'person': chosen_person}
    return render(request, person_details, person)
