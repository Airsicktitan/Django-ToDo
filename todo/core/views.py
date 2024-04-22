from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, EditToDo
from .models import toDoList
import datetime
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    todos = toDoList.objects.all().order_by('todo_title', 'todo_description')

    #This value caluculates the difference/time elapsed a To-Do item was created
    current_date = datetime.datetime.now().date()
    count_rows = todos.count()

    if request.user.is_authenticated:
        return render(request, 'core/home.html', {'todos': todos, 'current_date': current_date, 'count_rows': count_rows})
    else:
        return redirect('login')

def about(request):
    return render(request, 'core/about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in successfully!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again.")
            return redirect('login')
        
    else:
        return render(request, 'core/login.html', {})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You've successfully logged out!")
        return redirect('home')
    else:
        return redirect('login')

def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #login user
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You have registered succesfully!")
            return redirect('home')
        else:
            messages.success(request, "Whoops, there was a problem, please try again!")
            return redirect('register')
    else: 
        return render(request, 'core/register.html', {'form' : form})
    

def todo_detail(request, pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(toDoList, pk = pk)
        return render(request, 'core/todo_detail.html', {'todo' : todo})
    else:
        return redirect('login')

def delete_todo(request, pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(toDoList, pk = pk)
        
        todo.delete()
        messages.success(request, "Record Deleted!") 

        return redirect('home')
    else:
        return redirect('login')


def add_todo(request):
    form = EditToDo()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditToDo(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "You have added a new To-Do item succesfully! 🙌")
                return redirect('home')
            else:
                messages.success(request, "Whoops, there was a problem, please try again!")
                return redirect('add')
        else: 
            return render(request, 'core/add_todo.html', {'form' : form})
    else:
        return redirect('login')
    

def update_todo(request, pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(toDoList, pk = pk)
        form = EditToDo(request.POST or None, instance = current_record)

        if form.is_valid():
            form.save()
            messages.success(request, "You have updated the To-Do item succesfully! 👌")
            return redirect('home')
        else: 
            return render(request, 'core/update_todo.html', {'form' : form, 'todos': current_record})
    else:
        messages.success(request, "You must be logged in to do that")
        redirect('login')
