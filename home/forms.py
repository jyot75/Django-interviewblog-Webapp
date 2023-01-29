from django import forms
from .models import BlogPost

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