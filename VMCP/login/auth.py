
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.template.context import RequestContext
from ipware.ip import get_ip
import datetime

from .forms import login_info_form

from operations import op_mysql as db
from operations import op_token as token

def auth(request):
    ip = get_ip(request)
    if request.method == 'POST':
        form = login_info_form(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password']
            user_result=db.validate_user(username,password,ip)
            if user_result['result'] == 'true':
                check_token=token.check_token(str(user_result['user_id']))
                if check_token == 'true':
                    token_result=token.validate_token(str(user_result['user_id']))
                    if token_result['result'] == 'true':
                        return redirect('panel/')
                    else:
                        renew_token_result=token.renew_token(str(user_result['user_id']))
                        return redirect('/')
                else :
                    renew_token_result=token.renew_token(str(user_result['user_id']))
                    return redirect('/')
            else :
                return render(request, 'login/login_failed.html', {'form': form})
        else:
            return render(request, 'login/login_failed.html', {'form': form})
    else:
        return render(request, 'login/login_failed.html', {'form': form})