from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('user/', include('consumer.urls'))
    path('login/', views.consumer_log_in),
    path('register/', views.consumer_register),
    path('consumer_is_exist/', views.consumer_is_exist),
    path('formtest/', views.from_test)
]
