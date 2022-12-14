from django.shortcuts import render,HttpResponse, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={
        'tasks':tasks,
        'form':form 
    }

    print(tasks)
    return render(request,'task/list.html',context)

def update_task(request,pk):
    task= Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')



    context={
        'form':form
    }
    return render(request,'task/update_task.html',context)

def delete_task(request,pk):
    task= Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('/')
        
    context={
        'task':task
    }
    return render(request, 'task/delete.html',context)