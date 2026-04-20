from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, f'Thanks {name}, we received your message!')
        return render(request, 'pages/contact.html')
    return render(request, 'pages/contact.html')

# Create your views here.
