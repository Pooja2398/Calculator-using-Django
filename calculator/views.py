from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def calculator(request):
    return render (request, "calculator.html")


def evenorodd(request):
    c=''
    if request.method=='POST':
        n=int(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request, "evenorodd.html", {'c': c})

def marksheet(request):
    if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        n3=int(request.POST.get('num3'))
        n4=int(request.POST.get('num4'))
        n5=int(request.POST.get('num5'))
        t=n1+n2+n3+n4+n5
        p=t*100/500
        data={
            'total':t,
            'per':p
        }
        return render(request, "marksheet.html" ,data)
    return render(request, "marksheet.html")