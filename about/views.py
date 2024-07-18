from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")