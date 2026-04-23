from django.shortcuts import render
from apps.students.models import Student
from apps.attendance.models import Attendance
from django.contrib.auth.decorators import login_required  # ✅ add

@login_required   # ✅ add
def student_report(request):
    students = Student.objects.all()
    data = []

    for student in students:
        total = Attendance.objects.filter(student=student).count()
        present = Attendance.objects.filter(student=student, status=True).count()
        absent = total - present

        percentage = 0
        if total > 0:
            percentage = (present / total) * 100

        data.append({
            'student': student,
            'total': total,
            'present': present,
            'absent': absent,
            'percentage': round(percentage, 2)
        })

    return render(request, 'reports/report.html', {'data': data})