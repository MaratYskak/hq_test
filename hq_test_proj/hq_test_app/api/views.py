from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import CreateModelMixin
from hq_test_app.api.serializers import UserRegistrationSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer