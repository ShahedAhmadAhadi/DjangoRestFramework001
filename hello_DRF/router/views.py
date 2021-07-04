from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import check_for_language
from rest_framework.decorators import api_view
from .models import Employee

# Create your views here.

@api_view(['GET', 'POST'])
def create_records(request):
    if request.method == "POST":
        pass
    return render(request, './router/index.html')
