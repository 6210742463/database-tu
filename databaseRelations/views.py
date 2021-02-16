from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


def dashboard(request):
    data = Person.objects.all()
    return render(request, "CRUD/dashboard.html",{'data':data})

def create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        form.save()
        return redirect("/dashboard")
    else:
        form = PersonForm()
    return render(request, 'CRUD/create.html', {'form':form})

def edit(request, id):
    if request.method == "POST":
        row = Person.objects.get(id=id)
        form = PersonForm(instance=row, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        row = Person.objects.get(id=id)
        form = PersonForm(initial=row.__dict__)
    
    return render(request, 'CRUD/edit.html', {'form':form})

def removeData(request, id):
    data = Person.objects.get(id=id).delete()
    return redirect('/dashboard')

def title(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        newData = Title(name = name)
        newData.save()
        return redirect("/dashboard")
    return render(request, 'CRUD/title.html')

def county(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        newData = County(name = name)
        newData.save()
        return redirect("/dashboard")
    return render(request, 'CRUD/county.html')

def faculty(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        newData = Faculty(name = name)
        newData.save()
        return redirect("/dashboard")
    return render(request, 'CRUD/faculty.html')

def doSomething(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        newData = DoSomething(name = name)
        newData.save()
        return redirect("/dashboard")
    return render(request, 'CRUD/doSomething.html')
