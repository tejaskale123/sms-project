from django.contrib import admin
from .models import Enrollment

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')

admin.site.register(Enrollment, EnrollmentAdmin)    