"""
urls.py (project-level) - The MAIN URL MAP of your project.
Think of this like a post office.
When someone visits a URL, Django checks this file to know
which app should handle that request.

URL Pattern:
  '' (empty)        → goes to students app
  'admin/'          → goes to Django's built-in admin panel
"""

from django.contrib import admin      # Import the admin module
from django.urls import path, include # path = creates a URL route, include = connects to another urls.py

urlpatterns = [
    # When someone visits /admin/ → open the admin panel
    path('admin/', admin.site.urls),
    
    # When someone visits anything else → hand it to our 'students' app
    # include() means: "go look at students/urls.py for more details"
    path('', include('students.urls')),
]
