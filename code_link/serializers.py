from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team,TeamRelation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamRelationSerializer(serializers.Serializer):
    class Meta:
        model = TeamRelation
        fields = '__all__'