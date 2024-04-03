from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    return render(request, "app_trab/index.html")
def enre(request):
    return render(request,"app_trab/sla.html")
def curio(request):
    return render(request,"app_trab/curio.html")
def edit(request):
    return render(request,"app_trab/edit.html")