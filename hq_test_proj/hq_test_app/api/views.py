from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import CreateModelMixin
from .serializers import LessonViewSerializer, UserRegistrationSerializer, UserRetrieveSerializer, UserListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from django.contrib.auth.models import User
from rest_framework.decorators import action

from ..models import Lesson, LessonView


class UserViewSet(CreateModelMixin, ListModelMixin,
                  RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all().order_by("-id")
    # serializer_class = UserRegistrationSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationSerializer
        if self.action == ["retrieve", "me"]:
            return UserRetrieveSerializer
        return UserListSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset



class UserLessonsView(viewsets.ViewSet):
    """
    возвращает список уроков с информацией о статусе и времени просмотра для данного пользователя
    """
    serializer_class = LessonViewSerializer

    def list(self, request):
        user = request.user

        user_lessons = LessonView.objects.filter(user=user)

        serializer = LessonViewSerializer(user_lessons, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
