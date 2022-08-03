from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm,PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.


def index(request):
    posts = Post.objects.all()
    limit = 4
    paginator = Paginator(posts, limit)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    try:
        posts = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        posts = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        posts = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render(request,'blog/index.html', locals())


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

@login_required
def addpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
        return redirect("index")
    context = {
    
        'form': form
    }
    return render(request, 'blog/addpost.html', context)



def post_detail(request,slug):
    post =  Post.objects.filter(
        slug=slug
    ).first()
    if request.user==post.author:
        return render(request,'blog/detail.html',locals())
    else:

    
    
        # List of active comments for this post


        return render(request,'blog/detail.html',locals())