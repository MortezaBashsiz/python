
from django.shortcuts import render,redirect
from operations import op_logger as log
from django.contrib.auth.decorators import login_required
from .forms import dashboard_form

@login_required
def load_mng1_12h(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_12h.html', {'form': dashboard_form})
    else:
    	return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_1d(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_1d.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_2d(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_2d.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_3d(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_3d.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_7d(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_7d.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_1m(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_1M.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_2m(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_2M.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_3m(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_3M.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_1y(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_1y.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

@login_required
def load_mng1_2y(request):
    if request.method == 'GET':
        form = dashboard_form(request.GET)
        return render(request, 'panel/mng1_2y.html', {'form': dashboard_form})
    else:
        return render(request, 'login/login_failed.html', {'form': dashboard_form})

