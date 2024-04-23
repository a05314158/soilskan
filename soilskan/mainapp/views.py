from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'mainapp/index.html')


def about(request):
    return render(request,'mainapp/about.html')


def version(request):
    return HttpResponse("<h4>v 1.0.0</h4>")