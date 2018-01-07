
from django.contrib import admin
from django.urls import path
from login import views as login
from login import auth as auth
from panel import views as panel

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', panel.load_panel),
    path('login/', login.load_login),
    path('auth', auth.auth),
    path('panel/', panel.load_panel),
    path('cdr/', panel.load_cdr),
    path('cc/', panel.load_cc),
]
