from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/users/',
        'teams': 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/teams/',
        'activity': 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/activity/',
        'leaderboard': 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/leaderboard/',
        'workouts': 'https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/workouts/',
    })
