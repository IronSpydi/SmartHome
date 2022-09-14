
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]


class ControlSystemRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["serial_no"]


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]
