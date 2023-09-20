from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import CreateModelMixin
from hq_test_app.api.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hq_test_proj.hq_test_app.api.serializers import LessonSerializer

from hq_test_proj.hq_test_app.models import Lesson


class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class UserLessonsView(APIView):
    """
    возвращает список уроков с информацией о статусе и времени просмотра для данного пользователя
    """
    def get(self, request):
        user = request.user

        user_lessons = Lesson.objects.filter(lessonstatus__user=user, lessonstatus__status='Просмотрено')

        serializer = LessonSerializer(user_lessons, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)