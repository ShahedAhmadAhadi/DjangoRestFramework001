from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def create_records(request):
    return HttpResponse('<h1>working</h1>')
