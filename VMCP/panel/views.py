
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.context import RequestContext
import datetime

from .forms import dashboard_form

def load_panel(request):

    if request.method == 'POST':

        form = dashboard_form(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('all-borrowed') )

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = dashboard_form(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'panel/panel.html', {'form': form})
