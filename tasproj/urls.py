"""major_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login',views.login),
    path('signup',views.signup),
    path('contact',views.con),
    path('register',views.reg),
    path('signup',views.Userreg),
    path('register',views.prof),
    path('user',views.Userreg),
    path('profuser',views.prof),
    path('services',views.servicesignup),
    path('servicesreq',views.Servicereq),
    path('service',views.Servicereq),
    path('thank',views.thanks),
    path('prologin',views.professionalogin),
    path('adminlogin',views.adminlog),
    path('showtab',views.show),
    path('afterlogin',views.aflog),
    path('afterprlogin',views.afprlog),
    path('proftask',views.profshow),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    