
from django.contrib import admin
from django.urls import path
from login import views as login
from login import auth as auth
from panel import views as panel

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login.load_login),
    path('login/', login.load_login),
    path('auth', auth.my_view),
    path('panel/', panel.load_panel),
]
