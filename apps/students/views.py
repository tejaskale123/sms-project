from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


@login_required
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            roll_number=request.POST.get('roll'),
            email=request.POST.get('email'),
            department=request.POST.get('department')
        )
        return redirect('student_list')

    return render(request, 'students/add.html')


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll')
        student.email = request.POST.get('email')
        student.department = request.POST.get('department')
        student.save()
        return redirect('student_list')

    return render(request, 'students/edit.html', {'student': student})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete.html', {'student': student})