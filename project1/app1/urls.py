from django.urls import path
from.import views


urlpatterns = [
    path('sv/', views.studenView, name='student_url'),
    path('ss/', views.showStudentView, name='showstudent_url'),
    path('ds/<int:id>/', views.deleteStuView, name='deletestu_url'),
    path('us/<int:id>/', views.updateStuView, name='updatestu_url')
]