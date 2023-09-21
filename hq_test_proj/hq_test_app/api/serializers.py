from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Lesson, LessonView, Product

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
    
class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
    
class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['viewed', 'viewed_time_seconds', 'user', 'lesson', 'last_viewed_at']
        read_only_fields = ['viewed', 'last_viewed_at']

class ProductStatsSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    name = serializers.CharField()
    total_views = serializers.SerializerMethodField()
    total_view_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    def get_total_views(self, obj):
        return obj.total_views

    def get_total_view_time(self, obj):
        return obj.total_view_time or 0

    def get_total_students(self, obj):
        return obj.total_students

    def get_purchase_percentage(self, obj):
        total_users = User.objects.count()
        if total_users == 0:
            return 0
        return (obj.total_students / total_users) * 100