
from django.contrib import admin
from django.urls import path
from mariaApp import views
from mariaApp.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('sobre_nos', views.sobre_nos, name='sobre_nos'),
]
