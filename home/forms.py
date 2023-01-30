from django import forms
from .models import BlogPost
from accounts.models import NewUser
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('company', 'year', 'job_offer', 'profile', 'title', 'body')
        
        widgets = {
            'company': forms.TextInput(attrs={'class' : 'form-control'}),
            'year': forms.NumberInput(attrs={'class' : 'form-control', 'min': '2021'}),
            'job_offer': forms.Select(attrs={'class': 'form-control'}),
            'profile': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'profile': 'Job Profile',
            'body': ''
        }




class ChangingPassword(PasswordChangeForm):
     old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

     class Meta:
        model = NewUser
        fields = ('old_password', 'new_password1', 'new_password2')

    


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control mb-3'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control mb-4'}))
    username = forms.IntegerField(label='Student ID', min_value=200100000)
    email = forms.EmailField(label='Institute E-mail Address', widget=forms.EmailInput(attrs={'class': 'form-control mb-4'}))
    degree = forms.ChoiceField(label='Select Degree',choices=(("B.TECH",'B.TECH'),("M.TECH",'M.TECH'),("MSC",'MSC'))) 
    year = forms.IntegerField(label='Gradution Year', min_value=2021)
    program = forms.CharField(label='Program of Study', widget=forms.TextInput(attrs={'class' : 'form-control mb-4'}))
    
    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name','username', 'email', 'degree', 'year', 'program')
