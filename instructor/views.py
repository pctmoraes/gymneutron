from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Instructor
import re
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
import json

def instructor(request):
    if request.method == "GET":
        instructors_list = Instructor.objects.all()
        return render(request, 'instructor.html', {'instructors': instructors_list})
    
    elif request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cpf = request.POST.get('cpf')
        
        empty_field = str()
        if len(name) <= 0:
            empty_field +='Name, '
        if len(last_name) <= 0:
            empty_field +='Last name, '
        if len(email) <= 0:
            empty_field +='Email, '
        if len(phone) <= 0:
            empty_field +='Phone, '
        if len(cpf) <= 0:
            empty_field +='CPF'
        
        if not empty_field:
            instructor = Instructor.objects.filter(cpf=cpf)

            if instructor.exists():
                return render(request, 'instructor.html', {"message": "Instructor already exists", 'name':name, 'last_name':last_name, 'email':email, 'phone':phone, 'cpf':cpf})
            
            if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
                return render(request, 'instructor.html', {'name':name, 'last_name':last_name, 'phone':phone, 'cpf':cpf})           
        else:
            return render(request, 'instructor.html', {"message": "Field: " + empty_field + " cannot be empty", 'name':name, 'last_name':last_name, 'phone':phone, 'cpf':cpf, 'email':email, 'phone':phone})
        
        instructor = Instructor(
            name = name,
            last_name = last_name,
            email = email,
            phone = phone,
            cpf = cpf
        )
        instructor.save()

    return render(request, 'instructor.html')

def update_instructor(request, id):
    body = json.loads(request.body)

    name = body['name']
    last_name = body['last_name']
    email = body['email']
    cpf = body['cpf']
    phone = body['phone']

    instructor = get_object_or_404(Instructor, id=id)
    try:
        instructor.name = name
        instructor.last_name = last_name
        instructor.email = email
        instructor.cpf = cpf
        instructor.phone = phone
        instructor.save()
        return JsonResponse({'status': '200', 'name': name, 'last_name': last_name, 'email': email, 'cpf': cpf, 'phone': phone})
    except:
        return JsonResponse({'status': '500'})