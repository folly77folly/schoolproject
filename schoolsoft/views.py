from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect
from .models import Student
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'schoolsoft/index.html')

def sudent_list(request):
    studentlist = Student.objects.all()

    return render(request, 'schoolsoft/studentlist.html', {'studentlist': studentlist})

def details(request, student_id):
    studentrecord = Student.objects.get(pk = student_id)

    return render(request, 'schoolsoft/studentdetails.html', {'studentrecord': studentrecord})

def updatecgpa(request, student_id):
    studentrecord = Student.objects.get(pk = student_id)
    # cgpa_value = form.cleaned_data['cgpa']
    studentrecord.cgpa = request.POST['cgpa'] 
    # studentrecord.cgpa = request.form('cgpa').value()
    studentrecord.save()
    return HttpResponseRedirect(reverse( 'sch:students'))