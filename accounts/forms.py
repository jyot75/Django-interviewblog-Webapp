from django import forms
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.IntegerField(label='Student ID', min_value=201900000)
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    degree = forms.ChoiceField(label='Select Degree',choices=(("1",'B.TECH'),("2",'M.TECH'),("3",'MSC'))) 
    year = forms.IntegerField(label='Gradution Year', min_value=2021)
    program = forms.CharField(label='Program of Study', widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2', 'degree', 'year', 'program')









# class UserForm(forms.ModelForm):
#     username = forms.IntegerField()
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     password1 = forms.CharField(max_length=255)
#     password2 = forms.CharField(max_length=255)

#     class Meta:
#         model = User
#         fields = ("first_name","last_name","username","email","password1","password2")
        
#     widgets = {
#         'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
#         'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
#         'email': forms.EmailInput(attrs={'class': 'form-control'}),
#         'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#         'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#     }





# class UserCustomForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('degree', 'year', 'program')

#         # label = {

#         # }

#         widgets = {
#             'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'program': forms.TextInput(attrs={'class': 'form-control'})
#         }
