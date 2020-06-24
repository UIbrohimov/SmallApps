from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('post:list_view')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # # log the user in
            user = form.get_user()
            login(request, user)
            # return HttpResponse(user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('post:list_view')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post:list_view')

