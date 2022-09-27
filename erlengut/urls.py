
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
import juntagrico

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('juntagrico.urls')),
    re_path(r'^$', juntagrico.views.home),
    re_path(r'^impersonate/', include('impersonate.urls')),
]
