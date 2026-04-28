"""
views.py - The BRAIN of your app (Business Logic).

In Django, a "View" is a Python function (or class) that:
  1. Receives a web request (e.g. user visits /students/)
  2. Does some work (fetch data, save data, etc.)
  3. Returns a web response (usually an HTML page)

This is the "V" in Django's MVT pattern:
  M = Model (database)
  V = View (logic) ← YOU ARE HERE
  T = Template (HTML)

Flow:
  Browser → URL → View → Model → Template → Browser
"""

from django.shortcuts import render, redirect, get_object_or_404
# render        = combines a template + data and returns HTML
# redirect      = sends user to a different URL
# get_object_or_404 = gets a DB record OR shows "404 Not Found" page

from django.contrib import messages
# messages = Django's flash message system (success/error alerts)

from django.contrib.auth.decorators import login_required
# login_required = blocks the view if user is not logged in

from django.db.models import Q, Avg, Count
# Q = complex database queries (AND / OR conditions)
# Avg, Count = database aggregation functions

from .models import Student, Department   # Our database models
from .forms import StudentForm, DepartmentForm, SearchForm  # Our forms


# DASHBOARD VIEW
@login_required  # This decorator means: "User must be logged in to see this"
def dashboard(request):
    """
    The HOME PAGE of our app.
    Shows summary statistics like total students, departments, average GPA.
    """
    
    # Query the database for statistics
    total_students   = Student.objects.count()           # COUNT(*) in SQL
    active_students  = Student.objects.filter(is_active=True).count()
    total_depts      = Department.objects.count()
    
    # Avg() calculates the average of a field across all records
    avg_gpa_result   = Student.objects.aggregate(Avg('gpa'))
    avg_gpa          = avg_gpa_result['gpa__avg'] or 0   # Handle None if no students
    avg_gpa          = round(float(avg_gpa), 2)
    
    # Get student count grouped by year
    students_by_year = (
        Student.objects
        .values('year')          # GROUP BY year
        .annotate(count=Count('id'))  # COUNT students per year
        .order_by('year')
    )
    
    # Get recent 5 students added
    recent_students = Student.objects.order_by('-created_at')[:5]
    
    # Get department wise student count
    dept_stats = (
        Department.objects
        .annotate(student_count=Count('students'))
        .order_by('-student_count')
    )
    
    # 'context' = dictionary of data we pass to the HTML template
    context = {
        'total_students':   total_students,
        'active_students':  active_students,
        'inactive_students': total_students - active_students,
        'total_depts':      total_depts,
        'avg_gpa':          avg_gpa,
        'students_by_year': students_by_year,
        'recent_students':  recent_students,
        'dept_stats':       dept_stats,
    }
    
    # render() = load the HTML template and fill in the context data
    return render(request, 'students/dashboard.html', context)


# LIST ALL STUDENTS
@login_required
def student_list(request):
    """Shows a table of all students. Supports search and filter."""
    
    form = SearchForm(request.GET)  # GET = data from URL query string (?query=...)
    
    # Start with ALL students
    students = Student.objects.select_related('department')
    # select_related = fetch department data in the same DB query (performance optimization)
    
    query = ''
    dept_filter = request.GET.get('department', '')  # Get department filter from URL
    
    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        
        if query:
            students = students.filter(
                Q(first_name__icontains=query)   |
                Q(last_name__icontains=query)    |
                Q(roll_number__icontains=query)  |
                Q(email__icontains=query)
            )
    
    if dept_filter:
        # Filter by department ID
        students = students.filter(department__id=dept_filter)
    
    departments = Department.objects.all()  # For the filter dropdown
    
    context = {
        'students':    students,
        'form':        form,
        'departments': departments,
        'query':       query,
        'dept_filter': dept_filter,
        'total':       students.count(),
    }
    return render(request, 'students/student_list.html', context)


# STUDENT DETAIL
@login_required
def student_detail(request, pk):
    """
    Shows full details of ONE student.
    'pk' = primary key = the unique ID of the student in the database.
    """
    
    # get_object_or_404: tries to find Student with this pk
    # If not found → automatically shows a "404 Page Not Found" error
    student = get_object_or_404(Student, pk=pk)
    
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)


# ADD NEW STUDENT
@login_required
def student_add(request):
    """
    Handles TWO types of requests:
    
    GET request  → User visits the page → Show empty form
    POST request → User submits the form → Save data & redirect
    """
    
    if request.method == 'POST':
        # User submitted the form
        # request.POST = dictionary of form data submitted
        form = StudentForm(request.POST)
        
        if form.is_valid():
            # All validations passed — save to database
            student = form.save()
            
            # Show a success message (displayed in the template)
            messages.success(request, f'✅ Student "{student.get_full_name()}" added successfully!')
            
            # Redirect to student list page
            return redirect('student_list')
        else:
            # Form has errors — show them to the user
            messages.error(request, '❌ Please fix the errors below.')
    
    else:
        # GET request — show an empty form
        form = StudentForm()
    
    return render(request, 'students/student_form.html', {
        'form':  form,
        'title': 'Add New Student',
        'btn_label': 'Add Student'
    })


# EDIT EXISTING STUDENT
@login_required
def student_edit(request, pk):
    """Edit an existing student's information."""
    
    # First, find the student (or 404)
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        # instance=student means "update this existing record, don't create new one"
        form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Student "{student.get_full_name()}" updated successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, '❌ Please fix the errors below.')
    else:
        # Pre-fill the form with existing student data
        form = StudentForm(instance=student)
    
    return render(request, 'students/student_form.html', {
        'form':    form,
        'student': student,
        'title':   f'Edit: {student.get_full_name()}',
        'btn_label': 'Save Changes'
    })


# DELETE STUDENT
@login_required
def student_delete(request, pk):
    """Delete a student after confirmation."""
    
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        name = student.get_full_name()
        student.delete()  # Delete from database
        messages.success(request, f'🗑️ Student "{name}" has been deleted.')
        return redirect('student_list')
    
    # GET request = show confirmation page
    return render(request, 'students/student_confirm_delete.html', {'student': student})


# DEPARTMENTS
@login_required
def department_list(request):
    """List all departments with student count."""
    departments = Department.objects.annotate(
        student_count=Count('students')
    ).order_by('name')
    
    return render(request, 'students/department_list.html', {'departments': departments})


@login_required
def department_add(request):
    """Add a new department."""
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dept = form.save()
            messages.success(request, f'✅ Department "{dept.name}" added!')
            return redirect('department_list')
    else:
        form = DepartmentForm()
    
    return render(request, 'students/department_form.html', {
        'form': form, 'title': 'Add Department'
    })
