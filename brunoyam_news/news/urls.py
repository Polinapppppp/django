# news/urls.py
from django.urls import path
from . import views  # импорт views из текущего приложения

# УДАЛИТЕ эту строку - она вызывает циклический импорт!
# from brunoyam_news.urls import urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.index, name='index'),
    path('modul10/practic/', views.practic, name='practic'),
    path('modul10/z2/', views.z2, name='z2'),
    path('modul10/z3/', views.z3, name='z3'),
    path('modul10/base/', views.base, name='base'),
]