"""
URL configuration for SMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogout', views.logout, name="adminlogout"),

    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("viewstudents", views.viewstudents, name="viewstudents"),
    path("viewfacultys", views.viewfaculty, name="viewfacultys"),
    path("viewcourses", views.viewcourses, name="viewcourses"),

    path("admincourse", views.admincourse, name="admincourse"),
    path("adminstudent", views.adminstudent, name="adminstudent"),
    path("adminfaculty", views.adminfaculty, name="adminfaculty"),

    path("addcourses", views.addcourses, name="addcourses"),
    path("addfaculty", views.addfaculty, name="addfaculty"),
    path("addstudent", views.addstudent, name="addstudent"),

    path("insertcourse", views.insertcourse, name="insertcourse"),
    path("insertfaculty", views.insertfaculty,name="insertfaculty"),

    path("deletecourse", views.deletecourse, name="deletecourse"),


    path("coursedeletion/<int:cid>", views.coursedeletion, name="coursedeletion"),
]
