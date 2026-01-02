from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path, include

import os
@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        # fallback for localhost
        base_url = "/api/"
    return Response({
        'users': f'{base_url}users/',
        'teams': f'{base_url}teams/',
        'activities': f'{base_url}activities/',
        'workouts': f'{base_url}workouts/',
        'leaderboard': f'{base_url}leaderboard/',
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('api/', include(router.urls)),
]
