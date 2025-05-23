from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30, gender='Male'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony', age=35, gender='Male'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve', age=28, gender='Male'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha', age=32, gender='Female'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce', age=40, gender='Male'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team'),
            Team(_id=ObjectId(), name='Gold Team')
        ]
        Team.objects.bulk_create(teams)

        # Assign users to teams
        for team in teams:
            team.members.set(users)
            team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=120, date='2025-04-02'),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=90, date='2025-04-03'),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=30, date='2025-04-04'),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=teams[0], points=100),
            Leaderboard(_id=ObjectId(), team=teams[1], points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
