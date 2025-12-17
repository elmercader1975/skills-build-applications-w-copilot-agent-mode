
from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import models as djongo_models
from bson import ObjectId


class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    def __str__(self):
        return self.username


class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='activities')
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.workout} - {self.duration}min"


class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} - {self.score}"
