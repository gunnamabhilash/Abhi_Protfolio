from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')




from appname.models import Student

def students(request):
    student = Student.objects.all()
    context = {'student':student}
    return render(request, 'student.html', context)

	
#Class based views


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '_all_'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'CBV/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'CBV/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "_all_"
	template_name = 'CBV/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'CBV/studentdelete.html'
	success_url ="/"
        

