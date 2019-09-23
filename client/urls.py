from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('new', views.client_new, name='client_new'),
    path('update/<int:pk>', views.client_update, name='client_update'),
    path('search/', views.client_search, name='client_search'),
]