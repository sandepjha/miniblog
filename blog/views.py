from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import LoginForm, Student, LoginForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.

#base
def base(request):
    return render(request,'base.html')

#about
def about(request):
    return render(request,"about.html")

#home
def home(request):
    return render(request,"home.html")

#logout
def logout(request):
    return HttpResponseRedirect("/home/")

#contact
def contact(request):
    return render(request, "contact.html")

#dashboard
def dashboard(request):
    return render(request, "dashboard.html")

#login
def login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
    else:
        form = LoginForm()
    return render(request, "login.html", {'fm':form})

#Signup
def signup(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Student()
    return render(request,'signup.html',{'form':fm})