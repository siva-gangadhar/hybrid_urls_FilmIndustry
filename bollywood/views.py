from django.shortcuts import render
from django.http import HttpResponse

def king(request):
    return HttpResponse("<h1><i>sharukh khan is the king of bollywood</i></h1>")

def joker(request):
    return HttpResponse("<h1> Arjun kapoor is the joker of bollywood </h1>")

