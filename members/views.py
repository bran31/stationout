from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
from .decorators import *

# Create your views here.


@login_required(login_url='login')
def index(request):
    member = Profile.objects.all()
    context = {'member': member}
    return render(request, 'members/index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def out(request):
    sick = Quarintine.objects.all().order_by('last_name')
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
            return redirect('/out')
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
            return redirect('/out')
    context = {
        'form': form,
    }

    return render(request, 'members/addout.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def memberPage(request):
    member = Profile.objects.all().order_by('last_name')

    context = {
        'member': member
    }

    return render(request, 'members/members.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def memberProfileView(request, pk):
    memberprofile = Profile.objects.filter(id=pk)

    context = {
        'memberprofile': memberprofile,
    }

    return render(request, 'members/profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def addProfileView(request):
    form = AddMemberProfile()
    if request.method == 'POST':
        form = AddMemberProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members')
    context = {
        'form': form
    }
    return render(request, 'members/add_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def profileupdate(request, pk):
    member = Profile.objects.get(id=pk)
    form = AddMemberProfile(instance=member)

    if request.method == 'POST':
        form = AddMemberProfile(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/members')
    context = {
        'form': form,
    }

    return render(request, 'members/add_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def memberProfile(request, pk):
    member = Profile.objects.get(id=pk)

    context = {
        'member': member
    }
    return render(request, 'members/profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def socialProfile(request):
    member = Profile.objects.filter(
        lastfive__isnull=True).order_by('last_name')

    context = {
        'member': member
    }
    return render(request, 'members/members.html', context)


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

            message.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'members/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def tour1(request):
    member = Profile.objects.filter(tour='1')

    context = {
        'member': member
    }

    return render(request, 'members/tour.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def tour2(request):
    member = Profile.objects.filter(tour='2')

    context = {
        'member': member
    }

    return render(request, 'members/tour.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def tour3(request):
    member = Profile.objects.filter(tour='3')

    context = {
        'member': member
    }

    return render(request, 'members/tour.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def als(request):
    member = Profile.objects.filter(
        rank='Medic').order_by('ted', 'oda', 'lastfive')

    context = {
        'member': member
    }

    return render(request, 'members/als.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def officers(request):
    member = Profile.objects.filter(
        rank='Lt').order_by('ted', 'oda', 'lastfive')

    context = {
        'member': member
    }

    return render(request, 'members/officers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def bls(request):
    member = Profile.objects.filter(rank='EMT').order_by('oda', 'lastfive')

    context = {
        'member': member
    }

    return render(request, 'members/bls.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def aplt(request):
    member = Profile.objects.filter(platoon='A')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def bplt(request):
    member = Profile.objects.filter(platoon='B')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def cplt(request):
    member = Profile.objects.filter(platoon='C')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def eplt(request):
    member = Profile.objects.filter(platoon='E')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def fplt(request):
    member = Profile.objects.filter(platoon='F')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['officers'])
def otherplt(request):
    member = Profile.objects.filter(platoon='Other')

    context = {
        'member': member
    }

    return render(request, 'members/platoon.html', context)


def profileform(request):
    context = {

    }
    return render(request, 'members/profile_form.html', context)
