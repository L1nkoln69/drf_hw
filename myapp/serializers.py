from .models import Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    comment = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'post', 'comment']


class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['text', 'author']


class CommentSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['comment_text', 'post', 'user']
