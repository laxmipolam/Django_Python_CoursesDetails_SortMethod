from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('instructors/', views.InstructorListView.as_view(), name='instructors'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('mycourses/', views.registeredCourseByUser.as_view(), name='my-registered'),
    path('course/<uuid:pk>', views.change_data_faculty, name='change-data-faculty'),
    path('cc/sort', views.sort, name='sort'),
]