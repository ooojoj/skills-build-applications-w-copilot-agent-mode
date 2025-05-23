from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer, CustomJSONEncoder
from django.conf import settings

BASE_URL = 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev'

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class CustomJSONRenderer(JSONRenderer):
    encoder_class = CustomJSONEncoder

class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    renderer_classes = [CustomJSONRenderer]

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': f'{BASE_URL}/api/users/',
        'teams': f'{BASE_URL}/api/teams/',
        'activities': f'{BASE_URL}/api/activity/',  # Corrected path
        'leaderboard': f'{BASE_URL}/api/leaderboard/',
        'workouts': f'{BASE_URL}/api/workouts/',
    })
