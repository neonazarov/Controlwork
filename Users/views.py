from django.shortcuts import render
from .models import *

def index(request):
    users = UsersModel.objects.all()

    return render(request, 'index.html', {'users': users})


def add_user(request):
    return render(request, 'add_user.html')
