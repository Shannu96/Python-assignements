from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request,'FirstPage\homepage.html')

def Indexpage(request):
    return HttpResponse("Hello Welcome to Index Page!")