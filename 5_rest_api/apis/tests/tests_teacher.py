from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse
from apis.models import School, ClassRoom, Teacher

class TeacherAPITestCase(test.APITestCase):
    def setUp(self):
        force_user = User.objects.create(username="Force07")
        self.first_school = School.objects.create(name="First1")
        self.first_class_room = ClassRoom.objects.create(yearly="2024", room="A1", school=self.first_school)
        self.second_class_room = ClassRoom.objects.create(yearly="2024", room="A2", school=self.first_school)
        self.first_teacher = Teacher.objects.create(first_name="Johnny", last_name="Doesa", gender="Male")
        self.first_teacher.class_room.add(self.first_class_room)
        self.first_teacher.class_room.add(self.second_class_room)
        self.second_teacher = Teacher.objects.create(first_name="Jeff", last_name="Doesan", gender="Male")
        self.data = {"first_name": "John", "last_name": "Doe", "gender": "Male" }
        self.client.force_authenticate(user=force_user)
        self.teacher_list_url = reverse("v1:teacher-list")
        self.teacher_detail_url = reverse("v1:teacher-detail", kwargs={'pk': self.first_class_room.pk})
    
    def test_create_teacher(self):
        response = self.client.post(self.teacher_list_url, self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['first_name'], self.data['first_name'])
        self.assertEqual(response.data['last_name'], self.data['last_name'])
        self.assertEqual(response.data['gender'], self.data['gender'])
        
    def test_filter_school_name(self):
        filter_url = f'{self.teacher_list_url}?school_name={self.first_school.name}'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.first_teacher.first_name)
        self.assertEqual(response.data[0]['last_name'], self.first_teacher.last_name)
        self.assertEqual(response.data[0]['gender'], self.first_teacher.gender)
        
    def test_teacher_list(self):
        response = self.client.get(self.teacher_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Teacher.objects.count(), 2)

    def test_teacher_detail(self):
        response = self.client.get(self.teacher_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.first_teacher.id)
        self.assertEqual(response.data['first_name'], self.first_teacher.first_name)
        self.assertEqual(response.data['last_name'], self.first_teacher.last_name)
        self.assertEqual(response.data['gender'], self.first_teacher.gender)
        self.assertEqual(len(response.data['class_room']), 2)
    

    def test_update_teacher(self):
        response = self.client.put(self.teacher_detail_url, {"first_name": "Mes", "last_name": "Mue"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], "Mes")
        self.assertEqual(response.data['last_name'], "Mue")
        
    def test_delete_teacher(self):
        response = self.client.delete(self.teacher_detail_url)
        self.assertEqual(response.data, None)
        self.assertEqual(Teacher.objects.count(), 1)