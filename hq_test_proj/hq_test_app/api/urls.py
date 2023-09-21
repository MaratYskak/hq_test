from rest_framework.routers import SimpleRouter

from .views import UserViewSet, UserLessonsView, Subscribe, ProductStatsViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'lesson-status', UserLessonsView, basename="lesson-status")
router.register(r'subscribe', Subscribe, basename="subscribe")
router.register(r'stats', ProductStatsViewSet, basename="stats")

urlpatterns = router.urls