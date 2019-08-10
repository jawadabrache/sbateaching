from django.shortcuts import render
from django.utils import timezone
from .models import Faculty, Course, Teaching_Preference, Timeslot, Timeslot_Preference
from pulp import *

# Create your views here.
def faculty_list(request):
	facultys = Faculty.objects.order_by('name')
	return render(request, 'teaching/faculty_list.html', {'facultys': facultys})

def course_list(request):
	courses = Course.objects.order_by('identif')
	return render(request, 'teaching/course_list.html', {'courses': courses})

def timeslot_list(request):
	timeslots = Timeslot.objects.order_by('identif')
	return render(request, 'teaching/timeslot_list.html', {'timeslots': timeslots})

def teaching_preference_list(request):
	teaching_preferences = Teaching_Preference.objects.order_by('last_update')
	return render(request, 'teaching/teaching_preference_list.html', {'teaching_preferences': teaching_preferences})

def timeslot_preference_list(request):
	timeslot_preferences = Timeslot_Preference.objects.order_by('last_update')
	return render(request, 'teaching/timeslot_preference_list.html', {'timeslot_preferences': timeslot_preferences})

def assignment(request):
	faculty = Faculty.objects.all()
	courses = Course.objects.all()
	timeslots = Timeslot.objects.all()
	teaching_preferences = Teaching_Preference.objects.all()
	timeslot_preferences = Timeslot_Preference.objects.all()
	# Size and ranges
	num_faculty = Faculty.objects.count()
	num_courses = Course.objects.count()
	num_timeslots = Timeslot.objects.count()
	num_teaching_preferences = Teaching_Preference.objects.count()
	num_timeslot_preferences = Timeslot_Preference.objects.count()
	M = range(num_faculty)
	N = range(num_courses)
	T = range(num_timeslots)
	K = range(num_teaching_preferences)
	L = range(num_timeslot_preferences)
	# Define the problem
	prob = LpProblem("The assignment problem", LpMaximize)
	# Add variables
	x = LpVariable.dicts("assign_course_faculty",K,0) # x are the assignment course -> faculty (node a) variables
	y = LpVariable.dicts("assign_faculty_a_faculty_b",M,0) # y are the assignment faculty (node a) -> faculty (node b) variables
	z = LpVariable.dicts("assign_faculty_timeslot",L,0) # z are the assignment faculty (node b) -> timeslot variables
	# Add objective
	prob += lpSum([teaching_preferences[k].preference*x[k] for k in K]) + lpSum([timeslot_preferences[l].preference*z[l] for l in L]), "Total Preference Score"
	# Add constraints
	for n in N: prob += lpSum([x[k] for k in K if teaching_preferences[k].course.id == courses[n].id]) == courses[n].nbr_sections_offered
	for k in K: prob += x[k] <= teaching_preferences[k].course.nbr_sections_offered
	for m in M: prob += y[m] - lpSum([x[k] for k in K if teaching_preferences[k].faculty.id == faculty[m].id]) == 0
	for m in M: prob += y[m] <= faculty[m].max_nbr_sections_to_allocate
	for m in M: prob += y[m] >= faculty[m].min_nbr_sections_to_allocate
	for m in M: prob += lpSum(z[l] for l in L if timeslot_preferences[l].faculty.id == faculty[m].id) - y[m] == 0
	for t in T: prob += lpSum(z[l] for l in L if timeslot_preferences[l].ts.id == timeslots[t].id) <= timeslots[t].nbr_rooms_available
	for l in L: prob += z[l] <= 1
	# Solve
	prob.solve()
	# The Assignment found
	course_assignment_messages = []
	timeslot_assignment_messages = []
	for k in K:
		if x[k].varValue > 0.5:
			course_assignment_messages.append(str(int(x[k].varValue)) + " sections of " + teaching_preferences[k].course.identif + " assigned to " + teaching_preferences[k].faculty.name)
	for l in L:
		if z[l].varValue > 0.5:
			timeslot_assignment_messages.append(timeslot_preferences[l].ts.identif + " assigned to " + timeslot_preferences[l].faculty.name)
	return render(request, 'teaching/assignment.html', {
		'course_assignment_messages': course_assignment_messages,
		'timeslot_assignment_messages': timeslot_assignment_messages,
		})