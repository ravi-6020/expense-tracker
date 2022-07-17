# from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "signup.html"
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home.html')

def signupview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser =User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created")
        return redirect('/login')

    return render(request,"signup.html")



def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    expenses = Expense.objects.filter(user = request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type') 

        expense = Expense(name=text , amount=amount , expense_type=expense_type , user= request.user)
        expense.save()
        
        if expense_type == 'Positive':
            profile.balance += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
            
        profile.save()
        return redirect('/')

    context = {'profile' : profile , 'expenses' : expenses}
    return render(request , 'home.html' , context)