from django.db import models
from apps.students.models import Student

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_present = models.IntegerField()
    total_absent = models.IntegerField()