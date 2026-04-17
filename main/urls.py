from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UstozViewSet, GuruhViewSet, TalabaViewSet


router = DefaultRouter()


router.register(r'ustozlar', UstozViewSet, basename='ustoz')
router.register(r'guruhlar', GuruhViewSet, basename='guruh')
router.register(r'talabalar', TalabaViewSet, basename='talaba')

urlpatterns = [
    path('', include(router.urls)),
]