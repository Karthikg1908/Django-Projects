from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_registration, name='student_registration'),
    path('enroll/', views.enroll_course, name='enroll_course'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add_course/', views.add_course, name='add_course'),
]
