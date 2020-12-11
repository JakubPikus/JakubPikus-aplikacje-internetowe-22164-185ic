from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Mecz


class MeczSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'team_h', 'team_a', 'referre', 'clock', 'created_at', 'updated_at',)
        model = Mecz

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)