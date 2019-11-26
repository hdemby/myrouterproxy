from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Lists, Item

# Create your views here.
def index(response):
    #ls = Lists.objects.get(id=id)
    return render(response, "lists/base.html", {})

def home(response):
    return render(response, "lists/home.html", {})

def lists(response, id):
    return HttpResponse("<h2> The ToDo lists '%s'will be shown here</h2>" % id)

def tasks(response, id=1):
    item = Lists.objects.get(id=id)
    return HttpResponse("<h2>This is where you will see the tasks associated with todo list '%s' </h2>" % item.name)

