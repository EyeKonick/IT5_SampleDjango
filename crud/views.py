from django.shortcuts import render
from django.http import HttpResponse
from .models import Genders
from django.contrib import messages
# Create your views here.


def login(request):
    return(render(request, 'user/Login.html'))


def add_gender(request):

    try:
        if request.method == "POST":
            gender = request.POST.get('gender')

            Genders.objects.create(gender=gender).save()
            messages.success(request, 'Gender added succesfully!')
            return render(request, 'gender/AddGender.html')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occured during add gender: {e}')