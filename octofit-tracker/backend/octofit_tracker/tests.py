from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, LeaderboardEntry, ClubActivity

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team', 'members': []}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser')
        url = reverse('activity-list')
        data = {'user': user.id, 'activity_type': 'run', 'duration': 30, 'date': '2024-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Cardio', 'description': 'Cardio workout'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardEntryTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username='leaderboarduser')
        url = reverse('leaderboardentry-list')
        data = {'user': user.id, 'score': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ClubActivityTests(APITestCase):
    def test_create_club_activity(self):
        url = reverse('clubactivity-list')
        data = {
            'name': 'Manga Maniacs',
            'description': 'Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
            'schedule': 'Tuesdays at 7pm',
            'max_attendance': 15
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Manga Maniacs')
    
    def test_club_activity_max_attendance_validation(self):
        url = reverse('clubactivity-list')
        data = {
            'name': 'Test Club',
            'description': 'Test description',
            'schedule': 'Mondays at 6pm',
            'max_attendance': 0  # Invalid: should be at least 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
