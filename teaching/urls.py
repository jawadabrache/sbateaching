from django.urls import path
from . import views

urlpatterns = [
	path('faculty', views.faculty_list, name='faculty_list'),
	path('courses', views.course_list, name='course_list'),
	path('timeslots', views.timeslot_list, name='timeslot_list'),
	path('teaching_preferences', views.teaching_preference_list, name='teaching_preference_list'),
	path('timeslot_preferences', views.timeslot_preference_list, name='timeslot_preference_list'),
	path('assignment', views.assignment, name='assignment'),
]