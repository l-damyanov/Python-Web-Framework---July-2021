from django.shortcuts import render, redirect

from templates_advanced.pythons_app.forms import PythonCreateForm
from templates_advanced.pythons_app.models import Python


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        data = req.POST
        form = PythonCreateForm(data)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

