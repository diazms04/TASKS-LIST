from django.shortcuts import render, redirect
from .models import Task

def tasks_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'tasks/tasks_list.html', context)

def create_task(request):
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    wa = 1
    if new_title == "" or new_description == "":
        tasks = Task.objects.all()
        context = {"tasks": tasks, "error": "Title and description is required", "wa":wa}
        return render(request, "tasks/tasks_list.html", context)
    task = Task(title=new_title, description=new_description) 
    task.save()
    return redirect("/")

def delete_task(request,id):
    task= Task.objects.get(id=id)
    task.delete()
    return redirect('/')