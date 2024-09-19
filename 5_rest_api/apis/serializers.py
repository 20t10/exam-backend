from rest_framework import serializers
from apis.models import School, ClassRoom, Teacher, Student

# code here

class SchoolListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'short_title', 'address', ]

class SchoolDetailModelSerialzier(SchoolListModelSerializer):
    class Meta:
        model = SchoolListModelSerializer.Meta.model
        fields = SchoolListModelSerializer.Meta.fields + ['count_classroom', 'count_teacher', 'count_student']
        
        
class ClassRoomListModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'yearly', 'room', 'school',]

 
class TeacherModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']

class TeacherDetailModelSerialzier(TeacherModelSerialzier):
    class_room = ClassRoomListModelSerialzier(read_only=True, many=True) 
    class Meta:
        model = TeacherModelSerialzier.Meta.model
        fields = TeacherModelSerialzier.Meta.fields + ['class_room']
        
  
    
class StudentModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'class_room']

class StudentDetailModelSerialzier(serializers.ModelSerializer):
    class_room = ClassRoomListModelSerialzier(read_only=True)  # Add the classroom field to the serializer. Detail serializer for ClassRoom model.
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'class_room']


class ClassRoomDetailModelSerialzier(serializers.ModelSerializer):
    teacher_set = TeacherModelSerialzier(read_only=True, many=True)
    students = StudentModelSerialzier(read_only=True, many=True)
    class Meta:
        model = ClassRoomListModelSerialzier.Meta.model
        fields =  ClassRoomListModelSerialzier.Meta.fields + ['teacher_set', 'students']