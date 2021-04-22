from django import forms
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description']

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid username and/or password.')
            return HttpResponseRedirect(reverse("login"))
    else:
        if request.user.is_authenticated:
            return redirect("index")
        return render(request, "meet/login.html")



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            profile = Profile(user=user)
            profile.save()
            messages.success(request, f'Account created for {username}, You can now Log In!')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect("index")
        form = UserRegisterForm()
    return render(request, "meet/register.html", {"form": form})



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return HttpResponseRedirect(reverse("login"))



@login_required(login_url='/')
def index(request):
    return render(request, "meet/index.html")



@login_required(login_url='/')
def profile(request):
    if request.method == "POST":
        username = request.user.username
        user_info = UserUpdateForm(request.POST, instance=request.user)
        profile_info = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_info.is_valid() and profile_info.is_valid():
            user_info.save()
            profile_info.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('profile')
        else:
            temp = User.objects.filter(username=request.POST["username"]).first()
            if temp != None and temp.username != username:
                messages.error(request, f'The username " {request.POST["username"]} " you provided for the update already exists!')
            else:
                messages.error(request, f'The email " {request.POST["email"]} " you provided for the update is invalid')
            return redirect('profile')
    else:
        print(request.user.username)
        user_info = UserUpdateForm(instance=request.user)
        profile_info = ProfileUpdateForm(instance=request.user.profile)
        return render(request, "meet/profile.html", {
        "user_info": user_info, "profile_info": profile_info
        })
