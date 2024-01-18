from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required
def homepage(request):
    return render(request,'dashboard.html')

# @login_required
# def profileview(request):     
#     return render(request,'profileview.html')

# @login_required
def add_employee(request):
    return render(request,'add_employee.html')

# @login_required
def filter_employee(request):
    return render(request,'filter_employee.html')

# @login_required
# def calender(request):
#     return render(request,'calender.html')

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

# @login_required
def logout_user(request):
    return render(request,'logout.html')






