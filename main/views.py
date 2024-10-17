from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from main.models import *


# Create your views here.

@login_required
def profile(request):
    contex = {}
    return render(request, 'index.html', contex)

def login_page(request):
    contex = {}
    return render(request, 'login/login.html', contex)

def students(request):
    student = Student.objects.all()
    groups = Group.objects.all()
    contex = {'students': student, 'groups':groups}
    return render(request, 'students.html', contex)

def create_student(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        group_id = request.POST['group_id']
        group = Group.objects.get(id=group_id)
        if group:
            student = Student(first_name=first_name, last_name=last_name, contact=contact,group_id=group_id)
            student.save()
            messages.success(request, 'Student has been created!')
            return redirect('students-page')

        messages.error('Group not found')
        return redirect('students-page')

def delete_student(request, id):
    id = int(id)
    student = Student.objects.get(id=id)
    if student:
        student.delete()
        messages.success(request, 'Student has been deleted!')
        return redirect('students-page')
    messages.error('Student not found')
    return redirect('students-page')

def student_info(request, id):
    id = int(id)
    student = Student.objects.get(id=id)
    groups = Group.objects.all()
    if student:
        context = {'student': student,'groups':groups}
        return render(request, 'student_info.html', context)
    return redirect('students-page')

def info_change(request, id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        group_id = request.POST['group_id']
        group = Group.objects.get(id=group_id)
        student = Student.objects.get(id=id)
        if group and student:
            student.first_name=first_name
            student.last_name=last_name
            student.contact=contact
            student.group_id=group_id
            student.save()
            messages.success(request, 'Student info changed!')
            return redirect('students-page')
        messages.error('Group or student not found')
        return redirect('students-page')

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('profile')
        messages.error(request, 'Invalid username or password')
        return redirect('login-page')

    return redirect('login-page')

def logout_page(request):
    logout(request)
    return redirect('login-page')