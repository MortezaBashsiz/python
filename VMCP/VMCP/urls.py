
from django.contrib import admin
from django.urls import path
from login import views as login
from login import auth as auth
from panel import views as panel
from django.contrib.auth import views as login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.login, name='login_login'),
    # path('login/', login.load_login),
    path('login/', login.login, name='login_login'),
    path('auth', auth.auth),
    path(r'panel/', panel.load_panel),
]
