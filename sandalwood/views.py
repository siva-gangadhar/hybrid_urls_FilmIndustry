from django.shortcuts import render
from django.http import HttpResponse

def king(request):
    return HttpResponse("<h1><i>puneethRajkumar is the king of sandalwood</i></h1>")

def joker(request):
    return HttpResponse("<h1><i>srinu is the joker of sandalwood </i></h1>")

