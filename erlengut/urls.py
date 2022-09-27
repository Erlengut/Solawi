
from django.conf.urls import include, repath
from django.contrib import admin
import juntagrico

urlpatterns = [
    repath(r'^admin/', admin.site.urls),
    repath(r'^', include('juntagrico.urls')),
    repath(r'^$', juntagrico.views.home),
    repath(r'^impersonate/', include('impersonate.urls')),
]
