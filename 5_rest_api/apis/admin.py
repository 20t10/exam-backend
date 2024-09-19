from django.contrib import admin
from apis.models import School, ClassRoom, Teacher, Student
# Register your models here.


class AdminScholl(admin.ModelAdmin):
    pass
class AdminTeacher(admin.ModelAdmin):
    pass
class AdminClassRoom(admin.ModelAdmin):
    pass
class AdminTeacher(admin.ModelAdmin):
     pass
class AdminStudent(admin.ModelAdmin):
     pass

admin.site.register(School, AdminScholl)
admin.site.register(ClassRoom, AdminClassRoom)
admin.site.register(Teacher, AdminTeacher)
admin.site.register(Student, AdminStudent)