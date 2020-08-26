from django.urls import path
from . import views

app_name = 'flip'

urlpatterns = [
    path('', views.FlipListView.as_view(), name='index'),
    path('create/', views.FlipCreateView.as_view(), name='create'),
    path('ajax/', views.ajax, name='ajax')
]
