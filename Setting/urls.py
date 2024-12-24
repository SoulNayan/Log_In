"""
URL configuration for Setting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from polls.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('logout/',logout),
    path('sign_up/',sign_up),
    path('dashboard/',dashboard),
    path('add_staff/',add_staff),
    path('view_staff/',view_staff),
    path('editstaff/',editstaff),
    path('deletestaff/',deletestaff),
    path('deleteslider/',deleteslider),
    path('addslider/',addslider),
    path('viewslider/',viewslider),
    path('editslider/',editslider),
    path('edit_profile/',edit_profile),
    path('addcategories/',addcategories),
    path('viewcategories/',viewcategories),
    path('editcategories/',editcategories),
    path('deletecategories/',deletecategories),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)