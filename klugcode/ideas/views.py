from .models import Idea, Comment
from rest_framework import viewsets
from .serializer import IdeaSerializer, CommentSerializer

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

