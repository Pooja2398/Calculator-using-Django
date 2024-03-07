from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def calculator(request):
    return render (request, "calculator.html")
