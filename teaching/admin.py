from django.contrib import admin
from .models import Faculty, Course, Teaching_Preference, Timeslot, Timeslot_Preference

# Register your models here.

admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Teaching_Preference)
admin.site.register(Timeslot)
admin.site.register(Timeslot_Preference)

admin.site.site_header = "SBA Teaching Portal"
admin.site.site_title = "SBA Teaching Portal"
admin.site.index_title = "SBA Teaching Portal"