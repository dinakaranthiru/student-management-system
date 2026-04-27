"""
forms.py - HTML FORM DEFINITIONS for your app.

Django Forms = Python classes that automatically:
  ✅ Generate HTML <input> fields
  ✅ Validate user input (check if email is valid, if fields are empty, etc.)
  ✅ Show error messages

ModelForm = A special form that is directly linked to a Model.
It automatically creates form fields from your model fields.
"""

from django import forms          # Import Django's forms module
from .models import Student, Department  # Import our models


# ─────────────────────────────────────────────
# STUDENT FORM
# Used for both: Adding a new student AND Editing an existing student
# ─────────────────────────────────────────────
class StudentForm(forms.ModelForm):
    """
    ModelForm automatically creates form fields from the Student model.
    We just need to tell it:
      1. Which model to use (Student)
      2. Which fields to show
    """
    
    class Meta:
        model = Student  # Link this form to the Student model
        
        # fields = list of model fields to include in the form
        fields = [
            'roll_number', 'first_name', 'last_name',
            'email', 'phone', 'department', 'year', 'gpa', 'is_active'
        ]
        
        # widgets = customize how each field looks in HTML
        # We're adding CSS classes so our fields look nice
        widgets = {
            'roll_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. CS2024001'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'student@college.edu'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+91 98765 43210'
            }),
            'department': forms.Select(attrs={
                'class': 'form-input'
            }),
            'year': forms.Select(attrs={
                'class': 'form-input'
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-input',
                'step': '0.01',  # Allow decimals
                'min': '0',
                'max': '10'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
    
    def clean_gpa(self):
        """
        Custom validation for the GPA field.
        'clean_<fieldname>' methods are called automatically by Django.
        They must return the cleaned (validated) value or raise an error.
        """
        gpa = self.cleaned_data.get('gpa')  # Get the submitted GPA value
        
        if gpa is not None:
            if gpa < 0 or gpa > 10:
                # ValidationError = tell the user what's wrong
                raise forms.ValidationError("GPA must be between 0 and 10.")
        
        return gpa  # Return the valid value


# ─────────────────────────────────────────────
# DEPARTMENT FORM
# ─────────────────────────────────────────────
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Computer Science'
            }),
        }


# ─────────────────────────────────────────────
# SEARCH FORM
# A simple form just for searching students (not linked to a model)
# ─────────────────────────────────────────────
class SearchForm(forms.Form):
    """
    A plain Form (not ModelForm) because search is not saving data.
    """
    query = forms.CharField(
        max_length=100,
        required=False,  # Not required — user can submit empty search
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': '🔍 Search by name, roll number, or email...'
        })
    )
