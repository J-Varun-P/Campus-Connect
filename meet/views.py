import datetime
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Activity
from django.core.paginator import Paginator

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


class activity(forms.Form):
    title = forms.CharField(label="Title", max_length=128)
    description = forms.CharField(label="Description", widget=forms.Textarea)


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
    activities = Activity.objects.all().order_by('-time')
    paginator = Paginator(activities, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, "meet/index.html", {
    "activities": page_obj
    })



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
            lines = request.user.profile.description.splitlines()
            print("In profile")
            print(lines)
            temp = User.objects.filter(username=request.POST["username"]).first()
            if temp != None and temp.username != username:
                messages.error(request, f'The username " {request.POST["username"]} " you provided for the update already exists!')
            else:
                messages.error(request, f'The email " {request.POST["email"]} " you provided for the update is invalid')
            return redirect('profile')
    else:
        lines = request.user.profile.description.splitlines()
        user_info = UserUpdateForm(instance=request.user)
        profile_info = ProfileUpdateForm(instance=request.user.profile)
        return render(request, "meet/profile.html", {
        "user_info": user_info, "profile_info": profile_info, "lines": lines
        })



@login_required(login_url='/')
def PasswordChangeDone(request):
    messages.success(request, f'Your Password has been changed successfully!')
    return redirect('index')


@login_required(login_url='/')
def addactivity(request):
    if request.method == "POST":
        user_activity = activity(request.POST)
        if user_activity.is_valid():
            user_title = user_activity.cleaned_data["title"]
            user_description = user_activity.cleaned_data["description"]
            user_activity_create = Activity(user=request.user, title=user_title, description=user_description)
            print(user_activity_create)
            user_activity_create.save()
            messages.success(request, f'Your activity has been added successfully!')
            return redirect("index")
        else:
            return render(request, "meet/index.html", {
            "form": user_activity
            })
    else:
        user_activity = activity()
        return render(request, "meet/addactivity.html", {
        "form": user_activity
        })


@login_required(login_url='/')
def myactivities(request):
    activities = Activity.objects.filter(user=request.user)
    return render(request, "meet/myactivities.html", {
    "activities": activities
    })


@login_required(login_url='/')
def deleteactivity(request, id):
    activity = Activity.objects.get(pk=id)
    activity.delete()
    messages.success(request, f'Your activity has been deleted successfully!')
    return redirect("index")
