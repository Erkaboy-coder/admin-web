from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('login_page/', views.login_page, name='login-page'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('students/', views.students, name='students-page'),
    path('create_student/', views.create_student, name='create-student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete-student'),
    path('student_info/<int:id>/', views.student_info, name='student-info'),
    path('info_change/<int:id>/', views.info_change, name='info-change'),
]
