from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('firstweb/', views.firstweb, name='firstweb'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('thirdpage/', views.thirdpage, name='thirdpage'),
    path('person/', views.person, name='person'),
    path('history/', views.history, name='history'),
    path('product/', views.product, name='product'),
    path('ShowMyData', views.showMyData, name="ShowMyData"),
    path('inputProduct', views.inputProduct, name="inputProduct"),
    path('listProduct', views.listProduct, name="listProduct"),
]
