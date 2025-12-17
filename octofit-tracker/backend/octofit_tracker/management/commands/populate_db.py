from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        User = get_user_model()
        # Clear existing data in safe order for Djongo
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Running', description='Cardio endurance')

        # Create Activities
        Activity.objects.create(user=users[0], workout=workout1, duration=30, calories=200)
        Activity.objects.create(user=users[1], workout=workout2, duration=45, calories=350)
        Activity.objects.create(user=users[3], workout=workout1, duration=20, calories=120)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=500)
        Leaderboard.objects.create(user=users[1], score=450)
        Leaderboard.objects.create(user=users[3], score=600)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
