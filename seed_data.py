"""
seed_data.py - SAMPLE DATA LOADER

Run this script ONCE after migrations to fill your database
with demo data so you have something to show in your demo!

HOW TO RUN:
  python manage.py shell < seed_data.py

OR copy-paste into the Django shell:
  python manage.py shell
  >>> exec(open('seed_data.py').read())
"""
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

# We import our models to create records
from students.models import Student, Department

print("🌱 Seeding database with sample data...")

# ── Step 1: Clear existing data (optional, for fresh start) ──
Student.objects.all().delete()
Department.objects.all().delete()
print("  ✅ Cleared old data")

# ── Step 2: Create Departments ──
# objects.create() = INSERT INTO table VALUES (...)
cs   = Department.objects.create(name="Computer Science")
ec   = Department.objects.create(name="Electronics & Communication")
mech = Department.objects.create(name="Mechanical Engineering")
civil= Department.objects.create(name="Civil Engineering")
mba  = Department.objects.create(name="Business Administration")
print(f"  ✅ Created {Department.objects.count()} departments")

# ── Step 3: Create Students ──
students_data = [
    # (roll_number, first, last, email, phone, dept, year, gpa)
    ("CS2024001", "Arjun",    "Sharma",    "arjun.sharma@college.edu",    "9876543210", cs,    1, 9.2),
    ("CS2024002", "Priya",    "Patel",     "priya.patel@college.edu",     "9876543211", cs,    2, 8.7),
    ("CS2024003", "Rahul",    "Kumar",     "rahul.kumar@college.edu",     "9876543212", cs,    3, 7.5),
    ("CS2024004", "Sneha",    "Reddy",     "sneha.reddy@college.edu",     "9876543213", cs,    4, 9.5),
    ("EC2024001", "Vikram",   "Singh",     "vikram.singh@college.edu",    "9876543214", ec,    1, 8.1),
    ("EC2024002", "Anjali",   "Nair",      "anjali.nair@college.edu",     "9876543215", ec,    2, 7.8),
    ("ME2024001", "Karthik",  "Iyer",      "karthik.iyer@college.edu",    "9876543216", mech,  3, 6.9),
    ("ME2024002", "Deepa",    "Menon",     "deepa.menon@college.edu",     "9876543217", mech,  1, 8.4),
    ("CE2024001", "Arun",     "Krishnan",  "arun.krishnan@college.edu",   "9876543218", civil, 2, 7.2),
    ("MB2024001", "Lakshmi",  "Venkat",    "lakshmi.venkat@college.edu",  "9876543219", mba,   1, 8.9),
    ("CS2024005", "Nikhil",   "Joshi",     "nikhil.joshi@college.edu",    "9876543220", cs,    2, 5.5),  # Low GPA
    ("EC2024003", "Pooja",    "Mehta",     "pooja.mehta@college.edu",     "9876543221", ec,    4, 9.1),
]

for roll, first, last, email, phone, dept, year, gpa in students_data:
    Student.objects.create(
        roll_number = roll,
        first_name  = first,
        last_name   = last,
        email       = email,
        phone       = phone,
        department  = dept,
        year        = year,
        gpa         = gpa,
        is_active   = True
    )

# Mark one student as inactive for demo purposes
Student.objects.filter(roll_number="CS2024005").update(is_active=False)

print(f"  ✅ Created {Student.objects.count()} students")
print("\n🎉 Sample data loaded successfully!")
print("   You can now log in and explore the app.")
