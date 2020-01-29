from . import views
from django.urls import path

app_name = 'sch'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.sudent_list, name = 'students'),
    path('students/<int:student_id>', views.details, name = 'detail'),
    path('students/<int:student_id>/submit', views.updatecgpa, name = 'updatecgpa'),
]