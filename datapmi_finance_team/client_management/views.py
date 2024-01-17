from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse



def homepage(request):
    return render(request,'dashboard.html')


def profileview(request):
    return render(request,'profileview.html')

def add_employee(request):
    return render(request,'add_employee.html')

def filter_employee(request):
    return render(request,'filter_employee.html')

def calender(request):
    return render(request,'calender.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User(username=username,email=email)
        user.set_password(password)
        user.save()

        return redirect('login')

    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect ('homepage')
        else:
            return HttpResponse("Username or Password not Matched.")


    return render(request,'login.html')



def signout(request):
    logout(request)
    return redirect('login')



def logout(request):
    return render(request,'logout.html')



