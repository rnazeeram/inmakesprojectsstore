from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)

            return redirect('/')

        else:
            messages.info(request,'invalid username or password')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        email = request.POST['email']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        pswd=request.POST['password']
        cpswd = request.POST['cpassword']

        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username has already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email has already taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=uname,password=pswd,first_name=fname,last_name=lname,email=email)
                user.save();
                messages.info(request,'you have registered')
                return redirect('login')
            return redirect('/')

        else:
            messages.info(request,'!!password dose not match!!')


    return render(request,'register.html')