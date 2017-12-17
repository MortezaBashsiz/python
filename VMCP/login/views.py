
from django.shortcuts import render
from .forms import login_form

def load_login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            return render(request, 'login/login_login.html', {'form': login_form})
    else:
        return render(request, 'login/login_failed.html', {'form': login_form})

    

    