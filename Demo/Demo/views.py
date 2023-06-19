from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Blog
from .forms import StudentForm


def form(request):  
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = StudentForm()
    
    return render(request, 'form.html', {'form': form}) 


def index(request):
    post = Blog.objects.all()
    return render(request, "index.html", {'post': post})


def about(request):
    return render(request, "about.html")

def blog(request):
    post = Blog.objects.all()
    # Pass the post data to the template
    context = {
        'post': post,
    }
    
    # Render the template with the post data
    return render(request, 'blog.html', context)


def contact(request):
    return render(request, "contact.html")

def detail(request):
    return render(request, "detail.html")

def feature(request):
    return render(request, "feature.html")

def price(request):
    return render(request, "price.html")

def quote(request):
    return render(request, "quote.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})