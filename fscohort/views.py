from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from .forms import StudentForm
from .models import Student
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy # redirect görevini görüyor.

# Create your views here.

#########################################################
def home(request):
    return render(request, "fscohort/home.html")

# with class view template
class HomeView(TemplateView):
    template_name = "fscohort/home.html"
    
#########################################################

def student_list(request):
    
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)

# with class view template
class StudentListView(ListView):
    model  = Student
    # template_name = "fscohort/student_list.html" default name: app/modelname_list.html (templates klasörü altında aynı isimle olduğu için yazmaya gerek yok. "modelname" küçük harf ile olmalı)
    context_object_name = 'students' # default name : object_list

#########################################################

def student_add(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
            
    
    context = {
       
       "form":form     
    }
    
    return render(request, "fscohort/student_add.html", context)

# with class view template
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_add.html" 
    # default name: app/modelname_form.html(default name'e uyulmadığı için template_name yazdık)
    success_url = reverse_lazy("list")

#########################################################

def student_detail(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }
    
    return render(request, "fscohort/student_detail.html", context)

# with class view template
class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'
#########################################################

    
def student_update(request, id):
    
    student = Student.objects.get(id=id)
    
    form = StudentForm(instance=student)
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
       
    context= {
        
        "student":student,
        "form":form 
    }
    
    return render(request, "fscohort/student_update.html", context)

# with class view template


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html"
    success_url = reverse_lazy("list")


#########################################################

def student_delete(request, id):
    
    student = Student.objects.get(id=id)
   
    if request.method == "POST":

    
        student.delete()
        return redirect("list")
    
    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "fscohort/student_delete.html" # default name: app/modelname_confirm_delete.html
    success_url = reverse_lazy("list")
