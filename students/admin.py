"""
admin.py - Register your models with Django's Admin Panel.

Django has a FREE, built-in admin interface at /admin/
You can add, edit, delete records without writing any code!

To use it:
  1. Register your models here (this file)
  2. Create a superuser: python manage.py createsuperuser
  3. Visit: http://127.0.0.1:8000/admin/
"""

from django.contrib import admin  # Import the admin module
from .models import Student, Department  # Import our models


# ─────────────────────────────────────────────
# Customize how Student looks in the Admin panel
# ─────────────────────────────────────────────
@admin.register(Student)  # This decorator registers Student with the admin
class StudentAdmin(admin.ModelAdmin):
    
    # list_display = columns to show in the list view
    list_display = ['roll_number', 'first_name', 'last_name', 'department', 'year', 'gpa', 'is_active']
    
    # list_filter = filter sidebar on the right
    list_filter = ['department', 'year', 'is_active']
    
    # search_fields = enable the search bar
    search_fields = ['roll_number', 'first_name', 'last_name', 'email']
    
    # list_editable = edit these fields directly in the list view
    list_editable = ['is_active']
    
    # ordering = default sort order
    ordering = ['roll_number']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
