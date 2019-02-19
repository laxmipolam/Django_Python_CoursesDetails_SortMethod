from django.contrib import admin

# Register your models here.

from cc.models import Instructor, Major, Course, CourseInstance


#admin.site.register(Instructor)
# Define the Instructor class
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = ['first_name', 'last_name', 'date_of_birth']

# Register the admin class with the associated model
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Major)
#admin.site.register(Course)
#admin.site.register(CourseInstance)

# Register the Admin classes for Course using the decorator
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'showmajor')

# Register the Admin classes for LectureInstance using the decorator
@admin.register(CourseInstance) 
class CourseInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','regstudent','course')
  