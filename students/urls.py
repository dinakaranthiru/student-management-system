"""
urls.py (students app) - URL routes specific to the students app.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('login/',  auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Students
    path('students/',              views.student_list,   name='student_list'),
    path('students/add/',          views.student_add,    name='student_add'),
    path('students/<int:pk>/',     views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/',   views.student_edit,   name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Departments
    path('departments/',     views.department_list, name='department_list'),
    path('departments/add/', views.department_add,  name='department_add'),
]

