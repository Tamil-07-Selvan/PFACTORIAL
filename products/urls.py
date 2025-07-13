from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, CustomAuthToken, register, logout, profile

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/auth/register/', register, name='api_register'),
    path('api/auth/logout/', logout, name='api_logout'),
    path('api/auth/profile/', profile, name='api_profile'),
]