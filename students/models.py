"""
models.py - The DATABASE BLUEPRINT of your app.

A "Model" in Django = a table in your database.
Each class = one table.
Each variable inside the class = one column in that table.

Think of it like Excel:
  - Model class = Sheet name
  - Fields (variables) = Column headers
  - Each object you save = One row of data

Django will automatically CREATE the database table for you
when you run: python manage.py migrate
"""

from django.db import models  # Import Django's model tools


# ─────────────────────────────────────────────
# 1. DEPARTMENT MODEL
#    Represents a department like "Computer Science", "Mathematics"
# ─────────────────────────────────────────────
class Department(models.Model):
    """
    This creates a table called: students_department
    Columns: id (auto), name
    """
    
    # CharField = text field with a maximum length
    name = models.CharField(max_length=100)  # e.g. "Computer Science"
    
    def __str__(self):
        # __str__ controls what shows up when you print this object
        # Instead of showing "<Department object (1)>", it shows the name
        return self.name
    
    class Meta:
        # Meta = extra settings for this model
        ordering = ['name']  # Sort departments alphabetically by name


# ─────────────────────────────────────────────
# 2. STUDENT MODEL
#    Represents a student with all their info
# ─────────────────────────────────────────────
class Student(models.Model):
    """
    This creates a table called: students_student
    Columns: id, roll_number, first_name, last_name, email,
             phone, department, year, gpa, is_active, created_at
    """
    
    # CHOICES = a list of allowed values for a field
    # Format: (stored_value, display_label)
    YEAR_CHOICES = [
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    ]
    
    # ---- Basic Info ----
    roll_number = models.CharField(max_length=20, unique=True)
    # unique=True means no two students can have the same roll number
    
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    
    # EmailField = like CharField but validates email format
    email = models.EmailField(unique=True)
    
    # blank=True means this field is optional in forms
    phone = models.CharField(max_length=15, blank=True)
    
    # ---- Academic Info ----
    # ForeignKey = a relationship between two tables
    # One Department can have MANY Students → this is a Many-to-One relationship
    # on_delete=CASCADE means: if a department is deleted, delete its students too
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'  # lets us do: department.students.all()
    )
    
    year = models.IntegerField(choices=YEAR_CHOICES, default=1)
    
    # DecimalField = a number with decimal places (e.g. 8.75)
    # max_digits=4 means max 4 digits total (e.g. 10.00)
    # decimal_places=2 means 2 digits after decimal point
    gpa = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    
    # ---- Status ----
    # BooleanField = True or False
    is_active = models.BooleanField(default=True)
    
    # DateTimeField = stores date + time
    # auto_now_add=True = automatically sets to current time when created
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # When printed, show: "John Doe (CS2024001)"
        return f"{self.first_name} {self.last_name} ({self.roll_number})"
    
    def get_full_name(self):
        # A custom method to get the student's full name
        return f"{self.first_name} {self.last_name}"
    
    @property
    def gpa_grade(self):
        """Convert GPA to letter grade — this is a computed property (not stored in DB)"""
        gpa = float(self.gpa)
        if gpa >= 9.0: return 'A+'
        elif gpa >= 8.0: return 'A'
        elif gpa >= 7.0: return 'B'
        elif gpa >= 6.0: return 'C'
        else: return 'F'
    
    class Meta:
        ordering = ['roll_number']  # Sort students by roll number
