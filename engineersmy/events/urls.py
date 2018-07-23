from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<event_id>/detail/', views.detail, name='detail'),
    path('suggest/', views.suggest, name='suggest'),
]
