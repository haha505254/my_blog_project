from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'blog/index.html')


def sign_up(request):
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context)

def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  #重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'blog/login.html', context)

def log_out(request):
    logout(request)
    return redirect('Login') #重新導向到登入畫面