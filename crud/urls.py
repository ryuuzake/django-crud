from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nrp>/', views.detail, name='detail'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:nrp>/', views.update, name='update'),
    path('delete/<int:nrp>/', views.delete, name='delete')
]
