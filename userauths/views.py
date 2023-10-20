from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings 
# from django.contrib.auth import logout
from userauths.models import User

# Create your views here.

# User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, Your account was successfully created")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:home")
            # return redirect("userauth:sign-in")
        
    else:
        print("User can't be registered")
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey, you are already logged in")
        return redirect("core:home")
    
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.all(email=email)
            user = authenticate(request, email=email, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("core:home")
            else:
                messages.warning(request, "User does not exist. Create an account.")
        except:
            messages.warning(request, f"User with {email} doesn't exist")
     
    return render(request, "userauths/sign-in.html")



def logout_view(request):
    logout(request)
    messages.success(request, f"You logged out")
    return redirect("userauths:login")


    