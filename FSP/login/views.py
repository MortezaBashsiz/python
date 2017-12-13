from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.context import RequestContext
import datetime

from .models import RenewBookForm

def load_login(request):

    if request.method == 'POST':

        form = RenewBookForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('all-borrowed') )

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'login/index.html', {'form': form})