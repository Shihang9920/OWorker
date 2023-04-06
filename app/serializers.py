from rest_framework import serializers
from .models import Server
from django.contrib.auth.models import User


class ServerSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Server
        fields = '__all__'

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_owner(self, obj):
        return obj.owner.username
