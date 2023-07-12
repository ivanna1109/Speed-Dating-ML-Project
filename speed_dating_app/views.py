from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from .t_code import database_conn as db
from .t_code import ml_functions as ml

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

def submit_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = db.check_user(username, password)
    if (user == -1):
        context = {'message': 'User does not exist!'}
        return render(request, 'login.html', context)
    else:
        request.session['user'] = user
    persons = db.get_all_persons()
    paginator = Paginator(persons, 5)  # Podeli objekte na stranice sa po 10 elemenata
    page_number = request.GET.get('page')  # Preuzmi broj trenutne stranice iz zahteva
    page_obj = paginator.get_page(page_number) 
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)

def log_out(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    persons = db.get_all_persons()
    paginator = Paginator(persons, 5)  # Podeli objekte na stranice sa po 10 elemenata
    page_number = request.GET.get('page')  # Preuzmi broj trenutne stranice iz zahteva
    page_obj = paginator.get_page(page_number) 
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)

def person_details(request, parametar):
    print(parametar)
    chosen_person = db.find_person_by_ID(int(parametar))
    context = {'person': chosen_person}
    return render(request, 'person_details.html', context)

def my_profile(request):
    profile = db.find_person_by_ID(int(request.session['user']))
    context = {'person': profile}
    return render(request, 'person_details.html', context)

def top_matches(request):
    userId = request.session['user']
    user_doc = db.find_person_by_ID(userId)
    list_attr = create_list_attr(user_doc)
    top_matches_list = ml.most_resembling(list_attr)
    top_persons = db.find_top_matches(top_matches_list)
    context = {'top_matches': top_persons}
    return render(request, 'top_matches.html', context)

def create_list_attr(user_doc):
    list_attr = []
    list_attr.append(float(user_doc['gender']))
    list_attr.append(float(user_doc['age']))
    list_attr.append(float(user_doc['field_cd']))
    list_attr.append(float(user_doc['race']))
    list_attr.append(float(user_doc['imprace']))
    list_attr.append(float(user_doc['imprelig']))
    list_attr.append(float(user_doc['income']))
    list_attr.append(float(user_doc['goal']))
    list_attr.append(float(user_doc['date']))
    list_attr.append(float(user_doc['go_out']))
    list_attr.append(float(user_doc['sports']))
    list_attr.append(float(user_doc['tvsports']))
    list_attr.append(float(user_doc['exercise']))
    list_attr.append(float(user_doc['dining']))
    list_attr.append(float(user_doc['museums']))
    list_attr.append(float(user_doc['art']))
    list_attr.append(float(user_doc['hiking']))
    list_attr.append(float(user_doc['gaming']))
    list_attr.append(float(user_doc['clubbing']))
    list_attr.append(float(user_doc['reading']))
    list_attr.append(float(user_doc['tv']))
    list_attr.append(float(user_doc['theater']))
    list_attr.append(float(user_doc['movies']))
    list_attr.append(float(user_doc['concerts']))
    list_attr.append(float(user_doc['music']))
    list_attr.append(float(user_doc['shopping']))
    list_attr.append(float(user_doc['yoga']))
    list_attr.append(float(user_doc['attr1_1']))
    list_attr.append(float(user_doc['sinc1_1']))
    list_attr.append(float(user_doc['intel1_1']))
    list_attr.append(float(user_doc['fun1_1']))
    list_attr.append(float(user_doc['amb1_1']))
    list_attr.append(float(user_doc['shar1_1']))
    list_attr.append(float(user_doc['attr3_1']))
    list_attr.append(float(user_doc['sinc3_1']))
    list_attr.append(float(user_doc['intel3_1']))
    list_attr.append(float(user_doc['fun3_1']))
    list_attr.append(float(user_doc['amb3_1']))
    return list_attr