from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Faculty(models.Model):
	STATUS = (
		('Assis.', 'Assistant Professor'),
		('Assoc.', 'Associate Professor'),
		('Full', 'Full Professor'),
		('Lect.', 'Lecturer'),
		('Adjun.', 'Adjunct'),
	)
	name = models.CharField(max_length=80)
	status = models.CharField(max_length=6, choices=STATUS)
	min_nbr_sections_to_allocate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
	max_nbr_sections_to_allocate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
	def __str__(self):
		return self.name

class Course(models.Model):
	LEVEL = (
		('U', 'Undergraduate'),
		('G', 'Graduate'),
	)
	identif = models.CharField(max_length=7)
	name = models.CharField(max_length=60)
	level = models.CharField(max_length=1, choices=LEVEL)
	nbr_sections_offered = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
	def __str__(self):
		return '(' + self.identif+') - ' + self.name

class Teaching_Preference(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	last_update = models.DateField()
	preference = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
	comment = models.TextField()
	def __str__(self):
		return 'Pref. of ' + self.faculty.name + ' for ' + self.course.identif

class Timeslot(models.Model):
	TS = (
		('TR08000920', 'TR 8:00 - 9:20'),
		('TR09301050', 'TR 9:30 - 10:50'),
		('TR11001220', 'TR 11:00 - 12:20'),
		('TR12301350', 'TR 12:30 - 13:50'),
		('TR14001520', 'TR 14:00 - 15:20'),
		('TR15301650', 'TR 15:30 - 16:50'),
		('TR17001820', 'TR 17:00 - 18:20'),
		('TR18301950', 'TR 18:30 - 19:50'),
		('MWF08000850', 'MWF 8:00 - 8:50'),
		('MWF09000950', 'MWF 9:00 - 9:50'),
		('MWF10001050', 'MWF 10:00 - 10:50'),
		('MWF11001150', 'MWF 11:00 - 11:50'),
		('MWF12001250', 'MWF 12:00 - 12:50'),
		('MWF13401430', 'MWF 13:40 - 14:30'),
		('MW12001320', 'MW 12:00 - 13:20'),
		('MW15401700', 'MW 15:40 - 17:00'),
		('MW17101830', 'MW 17:10 - 18:30'),
	)
	identif = models.CharField(max_length=12, choices=TS)
	nbr_rooms_available = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
	def __str__(self):
		return self.identif

class Timeslot_Preference(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	ts = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
	last_update = models.DateField()
	preference = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
	comment = models.TextField()
	def __str__(self):
		return 'Pref. of ' + self.faculty.name + ' for ' + self.ts.identif