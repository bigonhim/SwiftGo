from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('materials/',views.materials,name='materials'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('contactInfo/',views.contactInfo,name='contactInfo'),
]