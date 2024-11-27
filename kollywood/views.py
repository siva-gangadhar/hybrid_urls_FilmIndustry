from django.shortcuts import render
from django.http import HttpResponse

def superstar(request):
    return HttpResponse("<h1><i>Rajini kanth is the king of kollywood</i></h1>")

def actress(request):
    return HttpResponse("<h1><i> Nayanathara is the  good actress of kollywood </i></h1>")

