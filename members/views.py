from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .filters import *
from .decorators import *

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = { }
    return render(request, 'members/index.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def out(request):
    sick = Quarintine.objects.all()
    myFilter = OutFilter(request.GET, queryset=sick)
    sick = myFilter.qs
    context = {
        'sick': sick, 'myFilter': myFilter,
    }
    return render(request, 'members/out.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def addout(request):
    form = SickForm()
    if request.method == 'POST':
        form = SickForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'members/addout.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def updateout(request, pk):
    member = Quarintine.objects.get(id=pk)
    form = SickForm(instance=member)

    if request.method == 'POST':
        form = SickForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form, 
    }
    
    return render(request, 'members/addout.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def memberPage(request):
    member = Profile.objects.all()

    context = {
        'member': member
    }
 
    return render(request, 'members/members.html', context)

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['officers'])
def memberProfile(request, pk):
    member = Profile.objects.get(id=pk)

    context = { 
        'member': member
    }
    return render(request, 'members/profile.html', context)

def returnPage(request):
    context = {}
    return render(request, 'members/return.html', context)



@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username or Password is incorrect')
            
    context = {}
    return render(request, 'members/login.html', context)

@unauthenticated_user 
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='members')
            user.groups.add(group)

            #message.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'members/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


