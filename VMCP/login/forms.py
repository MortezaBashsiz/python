
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class login_form(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data

class login_info_form(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'username',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'password',
        max_length = 32,
        widget = forms.PasswordInput()
    )