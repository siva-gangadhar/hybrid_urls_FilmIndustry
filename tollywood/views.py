from django.shortcuts import render
from django.http import HttpResponse

def superstar(request):
    return HttpResponse("<h1><i>vijayDevarakonda is the superstar of Tollywood</i></h1>")

def actress(request):
    return HttpResponse("<h1> <i>kaaj is the  good actress of tollywood</i> </h1>")

