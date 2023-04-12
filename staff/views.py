from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def login_user(request):
    ''' Utilising built in django authentication'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Login in Failed.'))
            return redirect('login_user')
    else:
        return render(request, 'staff-app/login.html', {})


def logout_user(request):
    ''' Utilising built in django authentication'''
    logout(request)
    # messages.success(request, ('great cheers...'))
    return redirect('home')


def change_password(request, user_id):
    ''' Utilising built in django authentication'''
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = ChangeUserPassword(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            messages.success(
                request, (f'Welcome {user}! \n Lets find you something to read...'))
            return redirect('profile', user_id)
    else:
        form = ChangeUserPassword(user=user)
    return render(request, 'staff-app/change_password.html', {'form': form, })
