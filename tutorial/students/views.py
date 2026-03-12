from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    student=[
        {'id':1,"name":"Atta","age":"25"}
    ]
    # return HttpResponse("<h2>Hello World<h2/>")
    return HttpResponse(student)