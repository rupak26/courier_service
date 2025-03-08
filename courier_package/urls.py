from django.urls import path 
from .views import PackageView

urlpatterns = [
     path('create/',PackageView.as_view(),name='packageManagement') ,
]