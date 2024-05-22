from rest_framework import routers
from django.urls import include, path
from .views import CommentViewSet, IdeaViewSet

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('aip-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


