
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import login_info_form

def auth(request):
    if request.method == 'POST':
        form = login_info_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel/')
        else:
            return render(request, 'login/login_failed.html', {'form': form})
    else:
        return render(request, 'login/login_failed.html', {'form': form})