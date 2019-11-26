from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('home/', views.home, name="Home"),
    path('lists/<int:id>', views.lists, name="Lists"),
    path(r'tasks/<int:id>', views.tasks, name="Tasks"),

]