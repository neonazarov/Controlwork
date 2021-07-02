from django.contrib import admin
from django.urls import path
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('', views.index),
    path('add_user', views.add_user),
]
