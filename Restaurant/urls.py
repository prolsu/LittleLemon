from django.contrib import admin
from django.urls import path, include
from . import views
from  .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('users', UserView.as_view()),
    path('menu', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('bookings', BookingView.as_view({'get':'list','post':'create'})),
    path('bookings/<int:pk>', BookingView.as_view({'get':'retrieve', 'put':'update','patch':'update','delete':'destroy'})),
]