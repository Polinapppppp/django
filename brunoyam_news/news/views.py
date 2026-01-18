from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request,'news/index.html')

def practic(request):
    return render(request, 'modul10/practic.html')
def z2(request):
    return render(request, 'modul10/z2.html')
def z3(request):
    return  render(request, 'modul10/z3.html')
def base(request):
    return  render(request, 'modul10/base.html')
