
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.template.context import RequestContext
import datetime

from .forms import login_info_form

from database import mariadb as db

def url_pars(url):
	return 200



def auth(request):

    if request.method == 'POST':

        form = login_info_form(request.POST)
        if form.is_valid():
        	userObj = form.cleaned_data
        	username = userObj['username']
        	password =  userObj['password']
        	result=db.auth(username,password)
        	if result == 'true':
        		return render(request, 'dashboard/index.html', {'form': form})
        	else :
        		return render(request, 'login/login_failed.html', {'form': form})
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = login_info_form(initial={'renewal_date': proposed_renewal_date,})