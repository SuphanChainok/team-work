from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name= 'index'),
    path('continue/', views.continue_view, name='continue'),
    path("map/", views.mappage, name= 'map'),

]
