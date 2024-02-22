from django.contrib import admin
from .models import Student,Admin,Course,Faculty
# Register your models here.

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Faculty)
