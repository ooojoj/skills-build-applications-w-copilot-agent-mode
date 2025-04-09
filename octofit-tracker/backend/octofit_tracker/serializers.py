from rest_framework import serializers
from bson import ObjectId
from rest_framework.utils.encoders import JSONEncoder
from .models import User, Team, Activity, Leaderboard, Workout

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId to string for JSON serialization
        if '_id' in representation:
            representation['_id'] = str(representation['_id'])
        if 'members' in representation:
            representation['members'] = [str(member) for member in representation['members']]
        return representation

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'type', 'duration', 'date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId to string for JSON serialization
        if '_id' in representation:
            representation['_id'] = str(representation['_id'])
        if 'user' in representation:
            representation['user'] = str(representation['user'])
        return representation

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
