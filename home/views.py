from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Message has been send!")

    return render(request, 'contact.html')