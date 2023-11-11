from django.urls import path
from . import views 


urlpatterns = [
    path('', views.clinicaKill),
    path('about/', views.about)   
]
