from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('login/', views.login, name='login'),
    path('person_details/<str:parametar>/', views.person_details, name='person_details')
]
