from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')


# Create your views here.
