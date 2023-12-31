from django.urls import path 
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path("sidebar/",views.sidebar,name="sidebar"),
    path("create/",views.create,name="create"),
    path("delete<int:id>/",views.delete,name="delete"),
    path("update<int:id>/",views.update,name="update"),
]