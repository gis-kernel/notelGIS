from django.shortcuts import render, redirect
from app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request, user)
                return render(request, 'gis/map.html', {})
            else:
                return HttpResponse("Account is not active")

        else:
            return HttpResponse('Username not matched')
    else:
        return render(request, 'nongis/index.html', {})


@login_required()
def user_logout(request):
    logout(request)
    return render(request, 'nongis/index.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            human = True
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'nongis/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def map(request):
    return render(request, 'gis/map.html')
