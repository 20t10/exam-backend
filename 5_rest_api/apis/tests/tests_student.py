from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse
from apis.models import School, ClassRoom, Student

class StudentAPITestCase(test.APITestCase):
    def setUp(self):
        force_user = User.objects.create(username="Force07")
        self.first_school = School.objects.create(name="First1")
        self.first_class_room = ClassRoom.objects.create(yearly="2024", room="A1", school=self.first_school)
        self.second_class_room = ClassRoom.objects.create(yearly="2024", room="A2", school=self.first_school)
        self.first_student = Student.objects.create(first_name="Braham", last_name="Eirson", gender="Male", class_room=self.first_class_room)
        self.second_student = Student.objects.create(first_name="Rylan", last_name="Steelcatcher", gender="Male", class_room=self.second_class_room)
        self.data = {"first_name": "John", "last_name": "Doe", "gender": "Male", "class_room": self.first_class_room.pk}
        self.client.force_authenticate(user=force_user)
        self.student_list_url = reverse("v1:student-list")
        self.student_detail_url = reverse("v1:student-detail", kwargs={'pk': self.first_class_room.pk})
    
    def test_create_student(self):
        response = self.client.post(self.student_list_url, self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['first_name'], self.data['first_name'])
        self.assertEqual(response.data['last_name'], self.data['last_name'])
        self.assertEqual(response.data['gender'], self.data['gender'])
        
    def test_filter_school_name(self):
        filter_url = f'{self.student_detail_url}?school_name={self.first_school.name}'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], self.first_student.first_name)
        self.assertEqual(response.data['last_name'], self.first_student.last_name)
        self.assertEqual(response.data['gender'], self.first_student.gender)
        
    def test_student_list(self):
        response = self.client.get(self.student_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 2)

    def test_student_detail(self):
        response = self.client.get(self.student_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.first_student.id)
        self.assertEqual(response.data['first_name'], self.first_student.first_name)
        self.assertEqual(response.data['last_name'], self.first_student.last_name)
        self.assertEqual(response.data['gender'], self.first_student.gender)
        self.assertEqual(response.data['class_room']['id'], self.first_student.class_room.id)
    

    def test_update_student(self):
        response = self.client.put(self.student_detail_url, {"first_name": "Mor", "last_name": "gott", "gender": "Omen", "class_room": self.second_class_room.pk}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], "Mor")
        self.assertEqual(response.data['last_name'], "gott")
        self.assertEqual(response.data['gender'], "Omen")
        self.assertEqual(response.data['class_room'], self.second_class_room.pk)
        
    def test_delete_student(self):
        response = self.client.delete(self.student_detail_url)
        self.assertEqual(response.data, None)
        self.assertEqual(Student.objects.count(), 1)