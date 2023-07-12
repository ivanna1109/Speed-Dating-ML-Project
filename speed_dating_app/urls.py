from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('login/', views.login, name='login'),
    path('submit_login/', views.submit_login, name='submit_login'),
    path('person_details/<str:parametar>/', views.person_details, name='person_details'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('top_matches/', views.top_matches, name='top_matches'),
    path('log_out/', views.log_out, name='log_out')
]
