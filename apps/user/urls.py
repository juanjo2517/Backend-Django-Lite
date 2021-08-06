# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'')

urlpatterns = [
    path('', include(router.urls))
]