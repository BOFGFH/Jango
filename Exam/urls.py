from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserListCreate, UserRetrieveUpdateDestroy

router = DefaultRouter()
router.register(r'users', UserListCreate)
router.register(r'users/(?P<pk>[^/.]+)', UserRetrieveUpdateDestroy)

urlpatterns = [
    path('', include(router.urls)),
]