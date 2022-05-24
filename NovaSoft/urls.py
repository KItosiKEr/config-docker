from django.urls import path, include
from rest_framework.routers import DefaultRouter

from NovaSoft.seriallizers import ContactSerializer
from .views import ContactVeiwSet, DeveloperViewSet

router = DefaultRouter()
router.register('developer', DeveloperViewSet, basename='dev')
router.register('contact', ContactVeiwSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))
]