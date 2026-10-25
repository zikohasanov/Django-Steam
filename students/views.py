from django.shortcuts import render
from .models import Students
def student_list(request):
    students= Students.objetcs.all()
    return render(request, 'students/student_list.html', {'students': students})