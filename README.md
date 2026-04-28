# 🎓 Student Management System
### Built with Python + Django | Demo Guide for Beginners

---

## 📁 PROJECT STRUCTURE

```
student_management/          ← Root folder
│
├── manage.py                ← Django's "remote control" (run commands here)
├── requirements.txt         ← List of packages to install
├── seed_data.py             ← Script to load sample data
├── db.sqlite3               ← Database file (created after migrations)
│
├── student_management/      ← Project configuration folder
│   ├── settings.py          ← All project settings (database, apps, etc.)
│   ├── urls.py              ← Main URL router
│   └── __init__.py          ← Makes this a Python package
│
├── students/                ← Our main app (the actual features)
│   ├── models.py            ← Database tables (Student, Department)
│   ├── views.py             ← Business logic (what happens on each page)
│   ├── forms.py             ← HTML form definitions & validation
│   ├── urls.py              ← URL routes for this app
│   ├── admin.py             ← Register models in Django Admin
│   └── apps.py              ← App configuration
│
└── templates/
    └── students/            ← All HTML files
        ├── base.html        ← Master layout (sidebar, header)
        ├── login.html       ← Login page
        ├── dashboard.html   ← Home page with stats
        ├── student_list.html       ← Table of all students
        ├── student_form.html       ← Add / Edit student form
        ├── student_detail.html     ← Single student profile
        ├── student_confirm_delete.html  ← Delete confirmation
        ├── department_list.html    ← List of departments
        └── department_form.html    ← Add department form
```

---

## 🚀 HOW TO RUN (Step by Step)

### Step 1 — Install Django
```bash
pip install django==4.2.7
```
> Django is the web framework. Think of it as the engine of your app.

### Step 2 — Go into the project folder
```bash
cd student_management
```

### Step 3 — Create the database
```bash
python manage.py migrate
```
> This reads your models.py and creates actual tables in db.sqlite3
> You'll see "OK" messages for each table created.

### Step 4 — Load sample data
```bash
python manage.py shell < seed_data.py
```
> This fills the database with 12 students and 5 departments for your demo.

### Step 5 — Create admin login
```bash
python manage.py createsuperuser
```
> Enter a username, email (optional), and password.
> You'll use this to log into the app.

### Step 6 — Start the server
```bash
python manage.py runserver
```
> This starts a local web server. You'll see:
> "Starting development server at http://127.0.0.1:8000/"

### Step 7 — Open the app
Open your browser and go to: **http://127.0.0.1:8000/**

## 🧠 KEY CONCEPTS 

| Concept |
|---------|-------------|
| **MVT Pattern** | Django uses Model-View-Template. Model = database, View = logic, Template = HTML |
| **ORM** | Instead of writing SQL, we write Python: `Student.objects.filter(year=1)` |
| **Migration** | When we change models.py, we run `makemigrations` + `migrate` to update the DB |
| **URL routing** | Django maps URLs to Python functions using urlpatterns in urls.py |
| **Templates** | HTML files with special Django tags like `{% for %}`, `{{ variable }}` |
| **Forms** | ModelForm automatically creates forms from your database models |
| **@login_required** | A decorator that protects pages from unauthenticated users |

---

## ⚡ QUICK COMMAND REFERENCE

```bash
python manage.py runserver          # Start the app
python manage.py migrate            # Apply database changes
python manage.py makemigrations     # Detect model changes
python manage.py createsuperuser    # Create admin user
python manage.py shell              # Open Python shell with Django loaded
```

---

*Built with ❤️ using Python 3 + Django 4.2*
