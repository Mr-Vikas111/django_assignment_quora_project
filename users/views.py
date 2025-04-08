
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# REGISTER FORM VIEW
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('_home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


# LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('_list_question')
                else:
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                messages.error(request, "No user with that email.")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# LOGOUT VIEW
def user_logout(request):
    logout(request)
    return redirect('_index')

