from django.shortcuts import render
from django.http import JsonResponse


def student(request):
    if request.method == 'GET':
        student = {
            'id':1, 
            'nome':'Carine'
        }
        return JsonResponse(student)
