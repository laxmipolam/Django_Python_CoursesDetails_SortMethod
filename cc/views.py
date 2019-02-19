from django.shortcuts import render

# Create your views here.

import datetime
import operator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from cc.forms import ChangeDataForm
from cc.forms import SortForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from cc.models import Course, Instructor, CourseInstance, Major

def sort(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SortForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            numbers = form.cleaned_data['numbers']
            numbers = numbers.replace(",", " ").split()
            order = form.cleaned_data['like']
            try:
            	p = list(map(int, numbers))
            	sortedNumbers = mySort(p, order)
            	error = False
            except:
            	error = True
            	sortedNumbers = "Give Valid Input"

            context = {
		'form': form,
                'numbers': sortedNumbers,
        	'submit': True,
                'error': error
            }
    else:
        form = SortForm()
        context = {
   	    'form': form,
            'submit': False,
        }
    return render(request, 'cc/sort.html', context)

def mySort(numbers,order):
    if len(numbers)>1:
        mid = len(numbers)//2
        lefthalf = numbers[:mid]
        righthalf = numbers[mid:]

        mySort(lefthalf, order)
        mySort(righthalf, order)

        p= 0
        q = 0
        r= 0
        operator = ""
        if(order == "Ascending"):
            while p < len(lefthalf) and q < len(righthalf):
                if lefthalf[p] < righthalf[q]:
                    numbers[r]=lefthalf[p]
                    p=p+1
                else:
                    numbers[r]=righthalf[q]
                    q=q+1
                r=r+1
        else:
            while p < len(lefthalf) and q < len(righthalf):
                if lefthalf[p] > righthalf[q]:
                    numbers[r]=lefthalf[p]
                    p=p+1
                else:
                    numbers[r]=righthalf[q]
                    q=q+1
                r=r+1
        while p < len(lefthalf):
            numbers[r]=lefthalf[p]
            p=p+1
            r=r+1

        while q < len(righthalf):
            numbers[r]=righthalf[q]
            q=q+1
            r=r+1
    return numbers
         

def index(request):
    num_courses = Course.objects.all().count()
    num_lectures = CourseInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_lectures_available = CourseInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_instructors = Instructor.objects.count()
    
    context = {
        'num_courses': num_courses,
        'num_lectures': num_lectures,
        'num_lectures_available': num_lectures_available,
        'num_instructors': num_instructors,
    }

    return render(request, 'index.html', context=context)



class CourseListView(generic.ListView):

    model = Course
    context_object_name = 'course'   
    #queryset = Course.objects.filter(title__icontains='')[:3]  
    template_name = 'course.html'  

class InstructorListView(generic.ListView):

    model = Instructor
    context_object_name = 'instructor'   
    template_name = 'instructor.html' 

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'coursedetail.html' 

class registeredCourseByUser(LoginRequiredMixin,generic.ListView):
    model = CourseInstance
    template_name ='cc/course_registered'
    
    def get_queryset(self):
        return CourseInstance.objects.filter(regstudent=self.request.user)

def change_data_faculty(request, pk):
    course_instance = get_object_or_404(CourseInstance, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ChangeDataForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            course_instance.next_registration =  form.cleaned_data['form_next_registration']
            course_instance.summary = form.cleaned_data['form_summary'] 
            course_instance.save()
            context = {
        	'form': form,
        	'course_instance': course_instance,
        	'submit': True,
                'mydate' : course_instance.next_registration +  datetime.timedelta(days=10)
 
            }

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_form_summary = course_instance.summary
        proposed_form_next_registration = course_instance.next_registration
        form = ChangeDataForm(initial={'form_next_registration': proposed_form_next_registration,'form_summary':proposed_form_summary})
        context = {
        'form': form,
        'course_instance': course_instance,
	'submit':False
        }
    
    return render(request, 'cc/change_data_faculty.html', context)

