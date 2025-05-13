from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = '__all__'

    def get_name(self, obj):
        return str(obj)  # Uses the model's __str__