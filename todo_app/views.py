from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    return render(request,'home.html')

@login_required(login_url='login')
def taskpage(request):
    if request.method == 'POST':
        task = request.POST.get('task') 
        new_todo =  Todo(user=request.user,task=task)  
        new_todo.save()

    all_tasks = Todo.objects.filter(user=request.user)  
    return render(request,'index.html',{'tasks':all_tasks})

def delete_task(request,id):
    get_task = Todo.objects.filter(user=request.user,id=id)
    get_task.delete()
    return redirect('tasks')

def finish_task(request,id):
    task = Todo.objects.filter(user=request.user,id=id).first()
    if task:
        task.status = True
        task.save()
    return redirect('tasks')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request,'register.html',{'form':form})

def login_site(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('tasks')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_site(request):
    logout(request)
    return redirect('home')