from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from passwordapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
	url(r'^register/',views.register),


]