from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse
from apis.models import School, ClassRoom

class ClassRoomAPITestCase(test.APITestCase):
    def setUp(self):
        force_user = User.objects.create(username="Force07")
        self.first_school = School.objects.create(name="First1")
        self.first_class_room = ClassRoom.objects.create(yearly="2024", room="1", school=self.first_school)
        self.data = {'yearly': "2025", "room": "1", "school": self.first_school.pk}
        self.client.force_authenticate(user=force_user)
        self.class_room_list_url = reverse("v1:classroom-list")
        self.class_room_detail_url = reverse("v1:classroom-detail", kwargs={'pk': self.first_class_room.pk})
    
    def test_create_school(self):
        response = self.client.post(self.class_room_list_url, self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['yearly'], self.data['yearly'])
        self.assertEqual(response.data['room'], self.data['room'])
        self.assertEqual(response.data['school'], self.data['school'])
        
    def test_filter_school(self):
        filter_url = f'{self.class_room_list_url}?school={self.first_school.pk}'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['yearly'], self.first_class_room.yearly)
        self.assertEqual(response.data[0]['room'], self.first_class_room.room)
        self.assertEqual(response.data[0]['school'], self.first_class_room.school.pk)
        
    def test_class_room_list(self):
        response = self.client.get(self.class_room_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ClassRoom.objects.count(), 1)

    def test_class_room_detail(self):
        response = self.client.get(self.class_room_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.first_class_room.id)
        self.assertEqual(response.data['yearly'], self.first_class_room.yearly)
        self.assertEqual(response.data['room'], self.first_class_room.room)
    

    def test_update_class_room(self):
        response = self.client.put(self.class_room_detail_url, {"yearly": "2026", "room": "A1"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['yearly'], "2026")
        self.assertEqual(response.data['room'], "A1")
        
    def test_delete_class_room(self):
        response = self.client.delete(self.class_room_detail_url)
        self.assertEqual(response.data, None)
        self.assertEqual(ClassRoom.objects.count(), 0)