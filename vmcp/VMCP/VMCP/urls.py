
from django.contrib import admin
from django.urls import path
from login import views as login
from login import auth as auth
from panel import views as panel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', panel.load_mng1_12h),
    path('login/', login.load_login),
    path('auth', auth.auth),
    path('mng1_12h.html/', panel.load_mng1_12h),
    path('mng1_1d.html/', panel.load_mng1_1d),
    path('mng1_2d.html/', panel.load_mng1_2d),
    path('mng1_3d.html/', panel.load_mng1_3d),
    path('mng1_7d.html/', panel.load_mng1_7d),
    path('mng1_1M.html/', panel.load_mng1_1m),
    path('mng1_2M.html/', panel.load_mng1_2m),
    path('mng1_3M.html/', panel.load_mng1_3m),
    path('mng1_1y.html/', panel.load_mng1_1y),
    path('mng1_2y.html/', panel.load_mng1_2y),
]
