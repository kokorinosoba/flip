from django.urls import path
from . import views

app_name = 'flip'

urlpatterns = [
    path('', views.FlipListView.as_view(), name='index'),
    path('create/', views.FlipCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.FlipUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.FlipDeleteView.as_view(), name='delete'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('ajax/', views.ajax, name='ajax'),
]
