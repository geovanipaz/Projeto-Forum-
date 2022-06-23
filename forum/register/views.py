from atexit import register
from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from register.forms import UpdateForm
from main.models import User
from django.contrib.auth import logout

# Create your views here.
def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('update_profile')
    context.update({
        'form':form,
        'title':'signup',
    })
    return render(request, 'register/signup.html', context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    context.update({
        'form':form,
        'title':'title',
    })
    return render(request, 'register/signin.html', context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    form = UpdateForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect('home')
    context.update({
        'form':form,
        'title':'title',
    })
    return render(request, 'register/update_profile.html', context)


@login_required
def logout(request):
    logout(request)
    return redirect('home')