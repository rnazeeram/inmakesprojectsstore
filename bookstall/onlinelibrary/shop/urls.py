from . import views
from django.urls import path
app_name='shop'
urlpatterns =[
path('',views.index,name='index'),
path('branches/',views.branches,name='branches'),
path('order/',views.order,name='order'),
# path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')#ajax
]
