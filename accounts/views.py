from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import UserForm

# Create your views here.

def landing_view(request):
    return render(request, 'landing.html')



# def register_view(request):
#     form = UserForm()
#     if request.method == 'POST':
#         form = UserForm(request.POST)

#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#             thisuser = authenticate(email=email, password=password)
#             login(request,thisuser)
#             return redirect('/home')
        
#     return render(request, 'register.html', {"form": form})




def register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        year = request.POST["year"]
        program = request.POST["program"]
        degree = request.POST["degree"]

        # if form.cleaned_data["password1"] != form.cleaned_data["password2"]:
        #     return render(request, 'register.html', {"error": "password not matches"})

        if form.is_valid():
            form.save()

            thisuser = User.objects.get(username=form.cleaned_data["username"])
            thisuser.profile.degree = degree
            thisuser.profile.year = year
            thisuser.profile.program = program
            thisuser.profile.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            thisuser = authenticate(request,username=username, password=password)
            login(request,thisuser)
            return redirect('/home')
        
    return render(request, 'register.html', {"form": form})




# def register_view(request):

#     if request.method == 'POST':
#         id = request.POST["student_id"]
#         f_name = request.POST["f_name"]
#         l_name = request.POST["l_name"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         conf_password = request.POST["conf_password"]
#         year = request.POST["year"]
#         program = request.POST["program"]
#         degree = request.POST["degree"]

#         if password != conf_password:
#             return render(request, 'register.html', {"error": "password not matches"})

#         if User.objects.filter(email=email).exists():
#             return render(request, 'register.html', {"error": "email is already in use"})

#         myuser = User.objects.create_user(username=id , email=email, password=password)
#         myuser.first_name = f_name
#         myuser.last_name = l_name
#         myuser.save()


#         thisuser = User.objects.get(username=myuser.username)
#         thisuser.profile.degree = degree
#         thisuser.profile.year = year
#         thisuser.profile.program = program
#         thisuser.profile.save()

#         messages.success(request, 'Account created successfully for Blog-it!!!')
#         thatuser = authenticate(request, username= myuser.username, password= myuser.password)
#         login(request, thatuser)
#         return redirect("/home")

#     return render(request, 'register.html')





def login_view(request):
    if request.user.is_authenticated:
        return redirect("/home")

    context = {}
    if request.method == 'POST':
        # username = request.POST["username"]
        email_user = request.POST["email_user"]
        password = request.POST["password"]

        username = email_user[0:9:1]
        # username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid email or password"}
            return render(request, 'login.html', context)
        login(request,user)
        return redirect("/home")

    return render(request, "login.html", context)



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login")


def change_pass(request):
    if request.user.is_authenticated:
        myuser = User.objects.get(username=request.user.username)
        myuser.set_password('jyot')
        myuser.save()
    else:
        return redirect('/login')
        
