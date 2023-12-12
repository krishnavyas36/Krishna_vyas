

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts}) 

def add(request):
    if request.method == 'POST':
        # Save form data
        return redirect('index') 
    else:     
        return render(request, 'add.html')