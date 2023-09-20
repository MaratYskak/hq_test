from rest_framework.routers import SimpleRouter

from hq_test_app.api.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")

urlpatterns = router.urls