from rest_framework import serializers

from apps.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            "rate": {"required": True},
            "content": {"required": True},
            "date_creation": {"required": False},
            "replies": {"required": False},
        }
