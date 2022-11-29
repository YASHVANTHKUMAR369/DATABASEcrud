from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.forms import StudentForm
def retrieve_view(request):
    students = Student.objects.all()
    return render(request,'crudApp/index.html', {'students':students})
    
def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudApp/create.html', {'form':form})
    
def delete_view(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect('/check')

    
def update_view(request,id):
    students = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudApp/update.html', {'students':students})
    
# Create your views here.
    