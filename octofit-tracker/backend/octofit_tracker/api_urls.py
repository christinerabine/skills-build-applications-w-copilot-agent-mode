from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet, ClubActivityViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'club-activities', ClubActivityViewSet)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path, include

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'workouts': '/api/workouts/',
        'leaderboard': '/api/leaderboard/',
        'club-activities': '/api/club-activities/',
    })

urlpatterns = [
    path('', include(router.urls)),
]
