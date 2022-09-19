from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    #path('Infos/',views.Infos.as_view(),name='info'),
     path('data/',views.data_view,name='data'),
     path('confirm/<pk>/',views.DeleteProduct.as_view(),name='delete'),
     path('Update/',views.update,name='update'),
     path('Condact/',views.contact,name='contact')

]
