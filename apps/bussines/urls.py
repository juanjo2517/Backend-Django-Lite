# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import bussines as bussines_view

router = DefaultRouter()
router.register(r'bussines', bussines_view.BussinesCompanyView, basename='bussines')

urlpatterns = [
    path('', include(router.urls))
]