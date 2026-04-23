from django.shortcuts import render, redirect
from apps.students.models import Student
from apps.subjects.models import Subject
from .models import Attendance
from django.contrib.auth.decorators import login_required

@login_required
def mark_attendance(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        status = request.POST.get('status')

        Attendance.objects.create(
            student_id=student_id,
            subject_id=subject_id,
            date=date,
            status=True if status == 'present' else False
        )
        return redirect('attendance_list')

    return render(request, 'attendance/mark.html', {
        'students': students,
        'subjects': subjects
    })


@login_required
def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/list.html', {'records': records})