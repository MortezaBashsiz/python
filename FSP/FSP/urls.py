
from django.contrib import admin
from django.urls import path
from login import views as login
from dashboard import views as dashboard

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login.load_login),
    path('dashboard/', dashboard.load_dashboard),
]
