from . import views
from django.urls import path
app_name='credentials'
urlpatterns = [
    path('register/',views.registration,name='register'),
    path('login1/',views.login1,name='login1'),
    path('logout/',views.logout,name='logout'),
]