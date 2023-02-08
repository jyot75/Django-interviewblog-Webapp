from django import forms
from accounts.models import NewUser
from django.contrib.auth.forms import SetPasswordForm


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New password",widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}),strip=False)

    new_password2 = forms.CharField(label="Confirm New password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

    class Meta:
        model = NewUser
        fields = '__all__'
