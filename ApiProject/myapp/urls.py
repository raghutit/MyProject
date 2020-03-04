from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MoviesViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register('movies', MoviesViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
