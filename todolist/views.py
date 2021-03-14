import requests
from django.shortcuts import render, redirect
from todolist.forms import TaskForm


def index(request):
    context = {}
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save() #version DB
            r = requests.post('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
            print(r)
        return redirect("index")
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos/')
    print("GET*: "+str(tasks.json()))
    context = {'tasks': tasks.json()}
    return render(request, "index.html", context=context)


def update_task(request, pk):
    #Récup le todo
    task = requests.get('https://jsonplaceholder.typicode.com/todos/'+str(pk))
    print("GET1: "+str(task.json()))
    context = {'task': task.json()}
    if request.method == "POST":
        r =requests.put('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
        print("PUT: "+str(r.json()))
        return redirect("index")
    return render(request, "update_task.html", context=context) #, {"task_edit_form": r}


def delete_task(request, pk):
    task = requests.delete('https://jsonplaceholder.typicode.com/todos/'+str(pk))
    print("DELETE: "+str(task.json()))
    return redirect("index")