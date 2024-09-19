from django.db import models



class School(models.Model):
    name = models.CharField(max_length=50, null=True)
    short_title = models.CharField(max_length=20, null=True)
    address = models.TextField()
    
    @property
    def count_classroom(self):
        return self.class_room.all().count()
    
    @property
    def count_teacher(self):
        return Teacher.objects.filter(class_room__school=self).distinct().count()
    
    @property
    def count_student(self):
        return Student.objects.filter(class_room__school=self).count()
    


class ClassRoom(models.Model):
    yearly = models.CharField(max_length=20)
    room = models.CharField(max_length=5)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, related_name="class_room")
    
    @property
    def count_teacher(self):
        return self.teacher_set.all().count()
    @property
    def count_student(self):
        return self.students.all().count()
   

class Teacher(models.Model):
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    gender = models.CharField(max_length=10, null=True)
    class_room = models.ManyToManyField(ClassRoom)


class Student(models.Model):
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    gender = models.CharField(max_length=10)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="students")
