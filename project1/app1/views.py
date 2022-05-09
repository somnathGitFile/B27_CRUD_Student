from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def studenView(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    context = {'form': form}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')
    return render(request, template_name, context)

def showStudentView(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updateStuView(request, id):
    obj = Student.objects.get(sid=id)
    template_name = 'app1/student.html'
    form = StudentForm(instance=obj)
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')
    return render(request, template_name, context)


def deleteStuView(request, id):
    obj = Student.objects.get(sid=id)
    template_name = 'app1/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showstudent_url')
    return render(request, template_name, context)

