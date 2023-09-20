from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import CreateModelMixin
from hq_test_app.api.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()