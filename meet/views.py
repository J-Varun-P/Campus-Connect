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
from .models import Profile, Activity, Joining, Comment, Deleted, Banneduser
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


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description']


class activity(forms.Form):
    title = forms.CharField(label="Title", max_length=128)
    description = forms.CharField(label="Description", widget=forms.Textarea)


class ActivityComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class comment(forms.Form):
    description = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write Something Here!"}))

class SearchActivity(forms.Form):
    username = forms.CharField(label="Username", max_length=128, required=False)
    title = forms.CharField(label="Title", max_length=128, required=False)


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
    if request.method == "POST":
        form = SearchActivity(request.POST)
        if form.is_valid():
            if form.cleaned_data["username"] == "" and form.cleaned_data["title"] == "":
                messages.error(request, 'Please provide at least one field input for search')
                return redirect("index")
            name = form.cleaned_data["username"]
            title = form.cleaned_data["title"]
            if name == "":
                name="empty_user"
            if title == "":
                title = "empty_title"
            return redirect("search_activities", name=name, title=title)
            return redirect("search_activities", name=form.cleaned_data["username"], title=form.cleaned_data["title"])
            return HttpResponse("Valid Searching...")
        return HttpResponse("Searching...")
    else:
        activities = Activity.objects.all().order_by('-time')
        activities_list = []
        deleted = Deleted.objects.all()
        for a in activities:
            obj = Deleted.objects.filter(activity=a).first()
            if obj is None:
                activities_list.append(a)
        paginator = Paginator(activities_list, 2)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        form = SearchActivity()
        return render(request, "meet/index.html", {
        "activities": page_obj, "form": form
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
            activity1 = Joining(user=request.user, activity=user_activity_create)
            activity1.save()
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

    deleted = Deleted.objects.all()
    deleted_list= []
    deleted_list_temp = []
    for x in deleted:
        deleted_list_temp.append(x.activity)

    joined = Joining.objects.filter(user=request.user).all()
    joined_list = []
    joined_list_temp = []
    for x in joined:
        joined_list_temp.append(x.activity)
    for a in joined:
        if a.activity not in deleted_list_temp:
            joined_list.append(a.activity)

    return render(request, "meet/myactivities.html", {
    "activities": joined_list
    })


@login_required(login_url='/')
def deletedactivities(request):
    deleted_list = []
    deleted = Deleted.objects.all()
    for a in deleted:
        users_list = []
        users_of_activity = list(Joining.objects.filter(activity = a.activity).all())
        for user in users_of_activity:
            users_list.append(user.user)
        if request.user in users_list:
            deleted_list.append(a.activity)
    return render(request, "meet/deletedactivities.html", {
    "activities": deleted_list
    })



@login_required(login_url='/')
def deleteactivity(request, id):
    activity = Activity.objects.get(pk=id)
    if request.user != activity.user:
        messages.error(request, f"You can not remove other's activities!")
        return redirect("index")
    user_activity = Deleted(activity=activity)
    user_activity.save()
    #activity.delete()
    messages.success(request, f'Your activity has been removed!')
    return redirect("deleted_activities")


@login_required(login_url='/')
def permanentdelete(request, id):
    activity = Activity.objects.get(pk=id)
    if request.user != activity.user:
        messages.error(request, f"You can not delete other's activities!")
        return redirect("index")
    activity.delete()
    messages.success(request, f'Your activity has been deleted successfully!')
    return redirect("index")


@login_required(login_url='/')
def commentdelete(request, id):
    comment = Comment.objects.get(pk=id)
    if request.user == comment.user or request.user == comment.activity.user:
        comment.delete()
    return redirect("display_activity", id=comment.activity.id)


@login_required(login_url='/')
def liveactivity(request, id):
    activity = Activity.objects.get(pk=id)
    if request.user != activity.user:
        messages.error(request, f"You can not make other's activities live!")
        return redirect("index")
    user_activity = Deleted.objects.get(activity=activity)
    user_activity.delete()
    messages.success(request, f'Your activity is now live!')
    return redirect("my_activities")


@login_required(login_url='/')
def displayactivity(request, id):
    if request.method == "POST":
        activity = Activity.objects.get(pk=id)
        user_comment = comment(request.POST)
        if user_comment.is_valid():
            obj = Comment(user=request.user, activity=activity, comment=user_comment.cleaned_data["description"])
            obj.save()
        return redirect("display_activity", id=id)
    else:
        activity = Activity.objects.get(pk=id)
        deleted = Deleted.objects.all()
        deleted_list= []
        users_list_temp = []
        for x in deleted:
            deleted_list.append(x.activity)
        if activity in deleted_list:
            users_of_activity = list(Joining.objects.filter(activity = activity).all())
            for user in users_of_activity:
                users_list_temp.append(user.user)
            if request.user not in users_list_temp:
                return redirect("index")
        users = Joining.objects.filter(activity=activity).all()
        users_comments=Comment.objects.filter(activity=activity)
        users_list = []
        for user in users:
            users_list.append(user.user.username)
        form = comment()
        print(request.user)
        print(activity.user)
        if request.user == activity.user:
            kickuserout = "True"
        else:
            kickuserout = "False"
        banned = Banneduser.objects.filter(activity=activity).all()
        banned_users = []
        for banned_user in banned:
            banned_users.append(banned_user.user)
        if request.user in banned_users:
            messages.error(request, f"You're banned from  {activity.title}  activity")
            return redirect("index")
        return render(request, "meet/activity.html", {
        "activity": activity, "users": users, "users_list": users_list, "form": form, "users_comments": users_comments, "kickuserout": kickuserout, "banned_users": banned_users
        })


@login_required(login_url='/')
def editactivity(request, id):
    obj = Activity.objects.get(pk=id)
    if request.method == "POST":
        form = ActivityUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Activity has been Edited successfully!')
            return redirect("index")
    if request.user == obj.user:
        form = ActivityUpdateForm(instance=obj)
        return render(request, "meet/editactivity.html", {
        "form": form
        })
    else:
        messages.error(request, f"You can not edit someone's activity")
        return redirect("index")


@login_required(login_url='/')
def joinactivity(request, id):
    obj = Activity.objects.get(pk=id)
    temp = Joining.objects.filter(user=request.user, activity=obj).first()
    if temp is not None:
        messages.error(request, f"Please don't mess with the url patterns, Thanks!")
        return redirect("index")
    activity_join = Joining(user=request.user, activity=obj)
    print(f"id is {request.user.id}")
    activity_join.save()
    return redirect("display_activity", id=id)


@login_required(login_url='/')
def leaveactivity(request, id):
    activity = Activity.objects.get(pk=id)
    temp = Joining.objects.filter(user=request.user, activity=activity).first()
    if temp is None:
        messages.error(request, f"Please don't mess with the url patterns, Thanks!")
        return redirect("index")
    obj = Joining.objects.get(user=request.user, activity=activity)
    obj.delete()
    return redirect("display_activity", id=id)


@login_required(login_url='/')
def searchactivities(request, name, title):
    count = 0
    if name != "empty_user":
        count = 1
        obj = User.objects.filter(username=name).first()
        if obj is None:
            messages.error(request, 'Username you provided does not exist')
            return redirect("index")
        activities = Activity.objects.filter(user=obj).order_by('-time')
    if title != "empty_title":
        if count == 0:
            activities = Activity.objects.filter(title__icontains=title).order_by('-time')
        else:
            obj = User.objects.filter(username=name).first()
            activities = Activity.objects.filter(user=obj, title__icontains=title).order_by('-time')
        if len(activities) == 0:
            messages.error(request, 'No activites matched your search activity field')
            return redirect("index")
    for a in activities:
        print(a)
    paginator = Paginator(activities, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, "meet/searchactivities.html", {
    "activities": page_obj, "name": name, "title": title
    })


@login_required(login_url='/')
def userprofile(request, name):
    obj = User.objects.get(username=name)
    lines = Profile.objects.get(user=obj).description.splitlines()
    if len(lines) == 1 and lines[0] == "Say Something about yourself!":
        lines[0] = "The User has not filled in their Profile yet!"
    return render(request, "meet/userprofile.html", {
    "lines": lines, "username": name
    })
    return HttpResponse(f"This is {name}'s profile'")



@login_required(login_url='/')
def kickuserout(request, u_id, a_id):
    user = User.objects.get(pk=u_id)
    activity = Activity.objects.get(pk=a_id)
    if request.user != activity.user:
        messages.error(request, f"Please don't mess with the url patterns, Thanks!")
        return redirect("index" )
    joining = Joining.objects.get(user=user, activity=activity)
    joining.delete()
    return redirect("display_activity", id=a_id)



@login_required(login_url='/')
def banuser(request, u_id, a_id):
    user = User.objects.get(pk=u_id)
    activity = Activity.objects.get(pk=a_id)
    if request.user == activity.user:
        ban_user = Banneduser(user=user, activity=activity)
        ban_user.save()
        joining = Joining.objects.filter(user=user, activity=activity).first()
        if joining is not None:
            joining.delete()
    return redirect("display_activity", id=activity.id)


@login_required(login_url='/')
def unbanuser(request, u_id, a_id):
    user = User.objects.get(pk=u_id)
    activity = Activity.objects.get(pk=a_id)
    if request.user == activity.user:
        ban_user = Banneduser.objects.get(user=user, activity=activity)
        ban_user.delete()
        joining = Joining(user=user, activity=activity)
        joining.save()
    return redirect("display_activity", id=activity.id)


@login_required(login_url='/')
def commentedit(request, id):
    obj = Comment.objects.filter(pk=id).first()
    if request.method == "POST":
        comment_form = ActivityComment(request.POST, instance=obj)
        if comment_form.is_valid():
            comment_form.save()
            return redirect("display_activity", id=obj.activity.id)
    if obj is None:
        messages.error(request, f"Please don't mess with the url patterns, Thanks!")
        return redirect("index")
    if request.user != obj.user:
        messages.error(request, f"You can not edit other's comments")
        return redirect("index")
    comment_form = ActivityComment(instance=obj)
    return render(request, "meet/editactivitycomment.html", {
    "form": comment_form
    })
