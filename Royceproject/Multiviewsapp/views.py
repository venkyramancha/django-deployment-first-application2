from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def f1(request):
    return HttpResponse("<h2>good mornng user....!! have a nice day...</h2><hr/>");
def f2(request):
    return HttpResponse("<h2>good afternoon user....!! hope you are doing good...</h2<hr/>");
def f3(request):
    return HttpResponse("<h2>good evening user...!!!how was your day...!!!</h2><hr/>");
