from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import groups_required


def sign_in(req):
    user = authenticate(username='pesho', password='1029384756qwe')
    login(req, user)
    return redirect('index')


def sign_out(req):
    logout(req)
    return redirect('index')


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


# @login_required(login_url="/sign_in")
@groups_required(groups=['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
