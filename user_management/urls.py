from django.urls import path 
from .views import UserRegistrationView , UserLoginView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='registration') ,
    path('login/',UserLoginView.as_view(),name='login'),
]