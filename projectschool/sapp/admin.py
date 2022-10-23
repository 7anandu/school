from django.contrib import admin
from .models import Course,Department,Person,Purpose
# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Purpose)
