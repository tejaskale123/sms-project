from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject


@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})


@login_required
def add_subject(request):
    if request.method == 'POST':
        Subject.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code')
        )
        return redirect('subject_list')

    return render(request, 'subjects/add.html')


@login_required
def delete_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('subject_list')