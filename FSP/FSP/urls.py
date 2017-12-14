
from django.contrib import admin
from django.urls import path
from login import views as login
from login import auth as auth
from dashboard import views as dashboard

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login.load_login),
    path('login/', login.load_login),
    path('auth', auth.auth),
    path('dashboard/', dashboard.load_dashboard),
]
