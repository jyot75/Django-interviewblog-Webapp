from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import NewUser
from .forms import SignupForm

# Create your views here.

def landing_view(request):
    return render(request, 'landing.html')



def register_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            thisuser = authenticate(request,username=username, password=password)
            login(request,thisuser)
            messages.success(request, 'Account created successfully for Blog-it!!!')
            return redirect('/home')
        
    return render(request, 'register.html', {"form": form})




def login_view(request):
    if request.user.is_authenticated:
        return redirect("/home")

    context = {}
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        username = NewUser.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid email or password"}
            return render(request, 'login.html', context)
        login(request,user)
        msg = "Welcome " + NewUser.objects.get(username=username).first_name + " !!"
        messages.success(request,msg)
        return redirect("/home")

    return render(request, "login.html", context)



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login")




def change_pass(request):
    if request.user.is_authenticated:
        myuser = NewUser.objects.get(username=request.user.username)
        myuser.set_password('jyot')
        myuser.save()
    else:
        return redirect('/login')

        
