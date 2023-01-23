from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Client
import re
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
import json

def client(request):
    if request.method == "GET":
        clients_list = Client.objects.all()
        if clients_list:
            return render(request, 'client.html', {'clients': clients_list})
        else:
            return render(request, 'client.html')
    
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
            client = Client.objects.filter(cpf=cpf)

            if client.exists():
                return render(request, 'client.html', {"message": "client already exists", 'name':name, 'last_name':last_name, 'email':email, 'phone':phone, 'cpf':cpf})
        
            if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
                return render(request, 'client.html', {'name':name, 'last_name':last_name, 'phone':phone, 'cpf':cpf})
            else:
                return render(request, 'client.html', {"message": "Field: " + empty_field + " cannot be empty", 'name':name, 'last_name':last_name, 'phone':phone, 'cpf':cpf, 'email':email, 'phone':phone})
        
        client = Client(
            name = name,
            last_name = last_name,
            email = email,
            phone = phone,
            cpf = cpf
        )
        client.save()          

    return render(request, 'client.html')
def update_client(id):
    print('the id:', id)
    return HttpResponse({"teste":1})
# def update_client(request, id):
#     body = json.loads(request.body)

#     name = body['name']
#     last_name = body['last_name']
#     email = body['email']
#     cpf = body['cpf']
#     phone = body['phone']

#     client = get_object_or_404(client, id=id)
#     try:
#         client.name = name
#         client.last_name = last_name
#         client.email = email
#         client.cpf = cpf
#         client.phone = phone
#         client.save()
#         return JsonResponse({'status': '200', 'name': name, 'last_name': last_name, 'email': email, 'cpf': cpf, 'phone': phone})
#     except:
#         return JsonResponse({'status': '500'})