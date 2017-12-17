
from django.shortcuts import render
from operations import op_logger as log
from django.contrib.auth.decorators import login_required
from .forms import dashboard_form

@login_required
def load_panel(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/panel.html', {'form': dashboard_form})
    else:
    	return render(request, 'login/login_failed.html', {'form': dashboard_form})