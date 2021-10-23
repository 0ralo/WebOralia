from rest_framework import serializers

from main.models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'date', 'author']
