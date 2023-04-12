from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class ChangeUserPassword(PasswordChangeForm):
    ''' Change password inherets from django password change form.
    Each form field utilises django widgets to give 
    it a from class of control from -
    Control form is a bootstrap from class.
    '''
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Retype New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = '__all__'
