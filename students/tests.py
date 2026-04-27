from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student, Department

# ════════════════════════════════════════════════════════
# 1. MODEL TESTS - Testing the Database Structure
# ════════════════════════════════════════════════════════
class StudentModelTest(TestCase):
    def setUp(self):
        # Create a test department
        self.dept = Department.objects.create(name="Computer Science")
        # Create a test student
        self.student = Student.objects.create(
            first_name="Test",
            last_name="User",
            roll_number="TEST001",
            department=self.dept,
            gpa=9.0,
            email="test@example.com"
        )

    def test_student_creation(self):
        """Test if the student is saved correctly in the DB"""
        self.assertEqual(self.student.first_name, "Test")
        self.assertEqual(self.student.roll_number, "TEST001")

    def test_student_full_name(self):
        """Test the get_full_name() property we wrote in models.py"""
        self.assertEqual(self.student.get_full_name(), "Test User")

# ════════════════════════════════════════════════════════
# 2. VIEW TESTS - Testing the Web Pages
# ════════════════════════════════════════════════════════
class StudentViewTests(TestCase):
    def setUp(self):
        # We need a client and a user because our pages are @login_required
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='password')
        self.dept = Department.objects.create(name="Engineering")

    def test_dashboard_redirect_if_not_logged_in(self):
        """If not logged in, user should be redirected to login page"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # 302 = Redirect
        self.assertIn('/login/', response.url)

    def test_dashboard_loads_after_login(self):
        """If logged in, dashboard should return HTTP 200 (Success)"""
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "📊 Dashboard")
