from rest_framework import serializers
from .models import DiscordUser


class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['id', 'background']
