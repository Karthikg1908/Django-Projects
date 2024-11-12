from django.shortcuts import render,get_object_or_404,redirect
from.models import Student,Course

def student_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        student = Student(first_name=first_name, last_name=last_name, email=email)
        student.save()
        return redirect('course_list')
    return render(request, 'courses/student_registration.html')

def enroll_course(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        course_id = request.POST['course_id']
        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Course, id=course_id)
        course.students.add(student)
        return redirect('course_list')
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'courses/enroll_course.html', {'students': students, 'courses': courses})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'students': students})

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        course = Course(name=name, description=description)
        course.save()
        return redirect('course_list')
    return render(request, 'courses/add_course.html')