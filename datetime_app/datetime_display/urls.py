from django.urls import include, path
from . import views
urlpatterns = [path('', views.current_datetime, name = 'currrent_datetime'),]