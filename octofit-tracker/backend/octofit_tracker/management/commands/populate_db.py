from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

# Sample data for users, teams, activities, leaderboard, and workouts
def get_sample_data():
    users = [
        {"name": "Tony Stark", "email": "tony@marvel.com", "team": "Marvel"},
        {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "Marvel"},
        {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "DC"},
        {"name": "Clark Kent", "email": "clark@dc.com", "team": "DC"},
    ]
    teams = [
        {"name": "Marvel", "description": "Earth's Mightiest Heroes"},
        {"name": "DC", "description": "Justice League"},
    ]
    activities = [
        {"user_email": "tony@marvel.com", "activity": "Running", "duration": 30},
        {"user_email": "steve@marvel.com", "activity": "Cycling", "duration": 45},
        {"user_email": "bruce@dc.com", "activity": "Swimming", "duration": 25},
        {"user_email": "clark@dc.com", "activity": "Flying", "duration": 60},
    ]
    leaderboard = [
        {"user_email": "clark@dc.com", "points": 100},
        {"user_email": "tony@marvel.com", "points": 90},
        {"user_email": "steve@marvel.com", "points": 80},
        {"user_email": "bruce@dc.com", "points": 70},
    ]
    workouts = [
        {"name": "Super Strength", "description": "Heavy lifting and power moves"},
        {"name": "Endurance", "description": "Long distance running and stamina"},
    ]
    return users, teams, activities, leaderboard, workouts

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        users, teams, activities, leaderboard, workouts = get_sample_data()

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert sample data
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        # Ensure unique index on email for users
        db.users.create_index([("email", ASCENDING)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
