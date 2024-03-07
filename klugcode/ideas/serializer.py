from .models import Idea, Comment
from rest_framework import serializers


class IdeaSerializer(serializers.HyperLinkedModels):
    class Meta:
        model = Idea

