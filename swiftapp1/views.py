from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def materials(request):
    materials = Material.objects.all()
    context = {
        'materials':materials
    }
    return render(request,'materials.html',context)
def contact(request):
    return render(request,'contact.html')

def contactInfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request,'contact.html')  
  
def details(request):
    return render(request,'materials-details.html')
