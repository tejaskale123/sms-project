from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.students.models import Student
from apps.subjects.models import Subject
from apps.attendance.models import Attendance

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):
    """
    Dashboard view to display key statistics.
    """
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()
    total_attendance = Attendance.objects.count()

    context = {
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_attendance': total_attendance,
    }

    return render(request, 'dashboard.html', context)


def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')