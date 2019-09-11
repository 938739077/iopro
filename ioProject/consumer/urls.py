from django.urls import path
from . import views

urlpatterns = [
    path('', views.path_only_user, name="user"),
    path('login/', views.consumer_log_in, name="login"),
    path('register/', views.consumer_register, name="register"),
    path('consumer_is_exist/', views.consumer_is_exist, name="consumer_is_exist"),
    path('interfaceTest/', views.interface_test, name="interface_test"),
    path('index/', views.index, name='index'),
    path('logout/', views.consumer_log_out, name="logout"),
]
