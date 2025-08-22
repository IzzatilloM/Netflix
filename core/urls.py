from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from main.views import ReviewViewSet, MovieViewSet, ActorViewSet

router = DefaultRouter()

router.register('reviews', ReviewViewSet)
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('example/', ExampleAPIView.as_view()),
    # path('actors/', ActorsAPIView.as_view()),
    # path('movies/',MoviesAPIView.as_view()),
    path('movies/<int:pk>/',MovieRetrieveUpdateDeleteAPIView.as_view()),
    path('subscription/', SubscriptionAPIView.as_view()),
    path('subscription/<int:pk>/', SubscriptionRetrieveUpdateDeleteAPIView.as_view()),
    path('', include(router.urls)),
]
