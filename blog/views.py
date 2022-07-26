from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request,'blog/index.html')


def sign_up(request):
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context)