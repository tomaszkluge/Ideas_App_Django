from .models import Idea, Comment
from rest_framework import serializers


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'websites', 'status']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['idea', 'reason']
