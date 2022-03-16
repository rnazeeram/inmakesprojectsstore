from . import views
from django.urls import path

urlpatterns = [
path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition')
   # path('',views.show,name='show'),
   # path('about/',views.about,name='about'),
   # path('contact/',views.contact,name='contact'),
   # path('details/',views.details,name='contact'),
    #path('thanks/',views.thanks,name='thanks')

]