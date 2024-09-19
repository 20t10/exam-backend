from django.test import TestCase
from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse
from apis.models import School

class SchoolAPITestCase(test.APITestCase):
    def setUp(self):
        force_user = User.objects.create(username="Force07")
        self.data = {'name': "Easton Magic Academy", "short_title": "EMA", "address": "33/66 somewhere someone earth 9432"}
        self.client.force_authenticate(user=force_user)
        self.school_list_url = reverse("v1:school-list")
        self.first_school = School.objects.create(name="First1")
        self.second_school = School.objects.create(name="S2secnond")
        self.school_detail_url = reverse("v1:school-detail", kwargs={'pk': self.first_school.pk})
    
    def test_create_school(self):
        response = self.client.post(self.school_list_url, self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['short_title'], self.data['short_title'])
        self.assertEqual(response.data['address'], self.data['address'])
        
    def test_filter_school_name(self):
        filter_url = f'{self.school_list_url}?name=S2'
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.second_school.name)
        
    def test_school_list(self):
        response = self.client.get(self.school_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], "First1")
        self.assertEqual(School.objects.count(), 2)

    def test_school_detail(self):
        response = self.client.get(self.school_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.first_school.id)
        self.assertEqual(response.data['name'], self.first_school.name)
    

    def test_update_school(self):
        response = self.client.put(self.school_detail_url, {"short_title": "F1", "address": "BangBangBang"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['short_title'], "F1")
        self.assertEqual(response.data['address'], "BangBangBang")
        
    def test_delete_school(self):
        response = self.client.delete(self.school_detail_url)
        self.assertEqual(response.data, None)
        self.assertEqual(School.objects.count(), 1)

