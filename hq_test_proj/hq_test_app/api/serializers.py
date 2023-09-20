from django.contrib.auth.models import User
from rest_framework import serializers

from hq_test_proj.hq_test_app.models import Lesson, LessonView

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration')

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ('lesson', 'user', 'viewed', 'viewed_time_seconds')
