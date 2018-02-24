from django.contrib import admin

# Register your models here.
from .models import Person, CMPUser, Question, Choice, Job, Employer

admin.site.register(Person)
admin.site.register(CMPUser)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Employer)
admin.site.register(Job)

