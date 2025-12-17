from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Workout, Activity, Leaderboard

class APISmokeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=123)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
