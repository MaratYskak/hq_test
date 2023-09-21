from rest_framework.routers import SimpleRouter

from .views import UserViewSet, UserLessonsView, Subscribe

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'lesson-status', UserLessonsView, basename="lesson-status")
router.register(r'subscribe', Subscribe, basename="subscribe")

urlpatterns = router.urls